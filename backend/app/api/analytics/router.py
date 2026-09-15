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

@router.get('/dashboard')
def get_dashboard_data(db: Session = Depends(get_db)):
    datasets_count = db.query(Dataset).count()
    return {
        "kpis": [
            {"title": "Total Datasets", "val": str(datasets_count), "pct": "+12%", "up": True},
            {"title": "Total Pipelines", "val": "8", "pct": "+5%", "up": True},
            {"title": "Total Reports", "val": "15", "pct": "+2.1%", "up": True},
            {"title": "Data Quality", "val": "98.5%", "pct": "+0.5%", "up": True},
        ],
        "revenueTrend": [
            {"name": "Jan", "value": 12}, {"name": "Feb", "value": 15},
            {"name": "Mar", "value": 14}, {"name": "Apr", "value": 20},
            {"name": "May", "value": 18}, {"name": "Jun", "value": 25},
            {"name": "Jul", "value": 22}, {"name": "Aug", "value": 30},
            {"name": "Sep", "value": 28}, {"name": "Oct", "value": 35},
            {"name": "Nov", "value": 34}, {"name": "Dec", "value": 40}
        ]
    }
