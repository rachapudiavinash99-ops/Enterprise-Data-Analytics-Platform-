from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.dataset import Dataset
from app.analytics_engine.query import execute_analytics_query
import pandas as pd
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class AnalyticsQuery(BaseModel):
    dataset_id: int
    group_by: List[str] = []
    metrics: List[Dict[str, str]]

@router.post('/query')
def run_query(query: AnalyticsQuery, db: Session = Depends(get_db)):
    dataset = db.query(Dataset).filter(Dataset.id == query.dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail='Dataset not found')
    try:
        df = pd.read_csv(dataset.file_path)
        result_df = execute_analytics_query(df, query.group_by, query.metrics)
        return result_df.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
