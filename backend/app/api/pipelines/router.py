from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.pipeline import Pipeline, PipelineExecution
from app.workers.pipeline_worker import execute_pipeline

router = APIRouter()

@router.post('/{pipeline_id}/execute')
def trigger_pipeline(pipeline_id: int, db: Session = Depends(get_db)):
    execution = PipelineExecution(pipeline_id=pipeline_id, status='running')
    db.add(execution)
    db.commit()
    # Trigger Celery task
    execute_pipeline.delay(pipeline_id)
    return {'message': 'Pipeline execution started', 'execution_id': execution.id}
