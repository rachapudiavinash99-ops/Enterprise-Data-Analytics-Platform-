from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.dataset import Dataset
from app.data_engine.profiler import profile_dataset
import os
import shutil
import uuid

router = APIRouter()
STORAGE_PATH = os.getenv('STORAGE_PATH', './storage')

def process_and_profile_dataset(dataset_id: int, file_path: str, db: Session):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        return
    
    try:
        profile = profile_dataset(file_path)
        dataset.profile_data = profile
        if 'error' in profile:
            dataset.status = 'failed'
        else:
            dataset.status = 'profiled'
            dataset.row_count = profile.get('row_count', 0)
            dataset.column_count = profile.get('column_count', 0)
        db.commit()
    except Exception as e:
        dataset.status = 'failed'
        db.commit()

@router.post('/upload')
def upload_dataset(background_tasks: BackgroundTasks, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(('.csv', '.xlsx', '.json')):
        raise HTTPException(status_code=400, detail='Invalid file type')
    
    os.makedirs(STORAGE_PATH, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_path = os.path.join(STORAGE_PATH, f"{file_id}_{file.filename}")
    
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    dataset = Dataset(
        name=file.filename,
        file_path=file_path,
        status='uploaded',
        file_size_bytes=os.path.getsize(file_path)
    )
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    
    background_tasks.add_task(process_and_profile_dataset, dataset.id, file_path, db)
    
    return {'id': dataset.id, 'name': dataset.name, 'status': 'processing'}
