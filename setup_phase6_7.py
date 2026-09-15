import os
import subprocess
import time

def run_git(cmd_args):
    subprocess.run(["git"] + cmd_args, check=True)

def create_file(path, content=""):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

commits = [
    {
        "msg": "Implement Analytics Query Engine",
        "files": {
            "backend/app/analytics_engine/query.py": "import pandas as pd\nfrom typing import List, Dict, Any\n\ndef execute_analytics_query(df: pd.DataFrame, group_by: List[str], metrics: List[Dict[str, str]]) -> pd.DataFrame:\n    # metrics format: [{'column': 'revenue', 'agg': 'sum'}]\n    agg_dict = {m['column']: m['agg'] for m in metrics}\n    if group_by:\n        return df.groupby(group_by).agg(agg_dict).reset_index()\n    else:\n        # Global aggregation without grouping\n        res = {}\n        for col, agg in agg_dict.items():\n            res[f\"{col}_{agg}\"] = df[col].agg(agg)\n        return pd.DataFrame([res])\n"
        }
    },
    {
        "msg": "Add Analytics router and schemas",
        "files": {
            "backend/app/api/analytics/router.py": "from fastapi import APIRouter, Depends, HTTPException\nfrom sqlalchemy.orm import Session\nfrom app.core.database import get_db\nfrom app.models.dataset import Dataset\nfrom app.analytics_engine.query import execute_analytics_query\nimport pandas as pd\nfrom pydantic import BaseModel\nfrom typing import List, Dict\n\nrouter = APIRouter()\n\nclass AnalyticsQuery(BaseModel):\n    dataset_id: int\n    group_by: List[str] = []\n    metrics: List[Dict[str, str]]\n\n@router.post('/query')\ndef run_query(query: AnalyticsQuery, db: Session = Depends(get_db)):\n    dataset = db.query(Dataset).filter(Dataset.id == query.dataset_id).first()\n    if not dataset:\n        raise HTTPException(status_code=404, detail='Dataset not found')\n    try:\n        df = pd.read_csv(dataset.file_path)\n        result_df = execute_analytics_query(df, query.group_by, query.metrics)\n        return result_df.to_dict(orient='records')\n    except Exception as e:\n        raise HTTPException(status_code=500, detail=str(e))\n"
        }
    },
    {
        "msg": "Add Dashboard and Widget models",
        "files": {
            "backend/app/models/dashboard.py": "from sqlalchemy import Column, Integer, String, ForeignKey, JSON\nfrom sqlalchemy.orm import relationship\nfrom app.core.database import Base\n\nclass Dashboard(Base):\n    __tablename__ = 'dashboards'\n    id = Column(Integer, primary_key=True, index=True)\n    name = Column(String, nullable=False)\n    description = Column(String)\n    organization_id = Column(Integer, ForeignKey('organizations.id'))\n    widgets = relationship('Widget', back_populates='dashboard')\n\nclass Widget(Base):\n    __tablename__ = 'widgets'\n    id = Column(Integer, primary_key=True, index=True)\n    dashboard_id = Column(Integer, ForeignKey('dashboards.id'))\n    title = Column(String, nullable=False)\n    widget_type = Column(String, nullable=False) # e.g., 'bar_chart', 'kpi'\n    config = Column(JSON, nullable=False) # Analytics query config\n    layout = Column(JSON, nullable=False) # x, y, w, h\n    dashboard = relationship('Dashboard', back_populates='widgets')\n"
        }
    },
    {
        "msg": "Add frontend Analytics and Dashboard pages",
        "files": {
            "frontend/package.json": '{"name": "enterprise-frontend", "version": "1.0.0", "scripts": {"dev": "vite"}, "dependencies": {"react-router-dom": "^6.20.0", "axios": "^1.6.0", "recharts": "^2.10.0"}}',
            "frontend/src/pages/Analytics.tsx": "import React from 'react';\n\nconst Analytics = () => {\n  return (\n    <div>\n      <h2>Analytics Engine</h2>\n      <div className='query-builder'>\n        <select><option>Sales Dataset</option></select>\n        <input type='text' placeholder='Group By (e.g., Region)' />\n        <input type='text' placeholder='Metric (e.g., Revenue)' />\n        <select><option>SUM</option><option>AVG</option></select>\n        <button>Run Query</button>\n      </div>\n      <div className='results'>\n        <p>Results will appear here...</p>\n      </div>\n    </div>\n  );\n};\n\nexport default Analytics;\n",
            "frontend/src/pages/Dashboards.tsx": "import React from 'react';\n\nconst Dashboards = () => {\n  return (\n    <div>\n      <h2>Interactive Dashboards</h2>\n      <button>Create New Dashboard</button>\n      <div className='dashboard-grid' style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginTop: '20px' }}>\n        <div className='widget' style={{ border: '1px solid #ccc', padding: '10px' }}>\n          <h4>Total Revenue</h4>\n          <h2>$1.2M</h2>\n        </div>\n        <div className='widget' style={{ border: '1px solid #ccc', padding: '10px' }}>\n          <h4>Sales by Region</h4>\n          <p>[ Bar Chart Placeholder ]</p>\n        </div>\n      </div>\n    </div>\n  );\n};\n\nexport default Dashboards;\n",
            "frontend/src/App.tsx": "import React from 'react';\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Login from './pages/Login';\nimport Dashboard from './pages/Dashboard';\nimport Organizations from './pages/Organizations';\nimport Users from './pages/Users';\nimport Datasets from './pages/Datasets';\nimport DataQuality from './pages/DataQuality';\nimport Pipelines from './pages/Pipelines';\nimport Analytics from './pages/Analytics';\nimport Dashboards from './pages/Dashboards';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path='/login' element={<Login />} />\n        <Route path='/' element={<Dashboard />} />\n        <Route path='/organizations' element={<Organizations />} />\n        <Route path='/users' element={<Users />} />\n        <Route path='/datasets' element={<Datasets />} />\n        <Route path='/quality' element={<DataQuality />} />\n        <Route path='/pipelines' element={<Pipelines />} />\n        <Route path='/analytics' element={<Analytics />} />\n        <Route path='/dashboards' element={<Dashboards />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n\nexport default App;\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Phase 6 and 7 commits created successfully.")
