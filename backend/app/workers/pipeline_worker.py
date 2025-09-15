from app.core.celery_app import celery_app
import time

@celery_app.task(name='execute_pipeline')
def execute_pipeline(pipeline_id: int):
    # Simulate pipeline node execution
    print(f'Starting pipeline {pipeline_id} execution...')
    time.sleep(2) # Load
    print('Cleaning data...')
    time.sleep(2) # Clean
    print('Transforming data...')
    time.sleep(2) # Transform
    print(f'Pipeline {pipeline_id} completed successfully.')
    return {'status': 'completed', 'pipeline_id': pipeline_id}
