from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.dataset import Dataset
import os
import shutil
import uuid

router = APIRouter()
STORAGE_PATH = os.getenv('STORAGE_PATH', './storage')

@router.post('/upload')
def upload_dataset(file: UploadFile = File(...), db: Session = Depends(get_db)):
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
    return {'id': dataset.id, 'name': dataset.name, 'status': dataset.status}
