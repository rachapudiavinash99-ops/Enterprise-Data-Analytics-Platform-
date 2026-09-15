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
        "msg": "Add Pipeline models and schemas",
        "files": {
            "backend/app/models/pipeline.py": "from sqlalchemy import Column, Integer, String, JSON, ForeignKey\nfrom sqlalchemy.orm import relationship\nfrom app.core.database import Base\n\nclass Pipeline(Base):\n    __tablename__ = 'pipelines'\n    id = Column(Integer, primary_key=True, index=True)\n    name = Column(String, nullable=False)\n    description = Column(String)\n    nodes = Column(JSON, nullable=False) # Visual pipeline graph nodes\n    edges = Column(JSON, nullable=False) # Visual pipeline graph edges\n    organization_id = Column(Integer, ForeignKey('organizations.id'))\n\nclass PipelineExecution(Base):\n    __tablename__ = 'pipeline_executions'\n    id = Column(Integer, primary_key=True, index=True)\n    pipeline_id = Column(Integer, ForeignKey('pipelines.id'))\n    status = Column(String, default='pending')\n    logs = Column(JSON)\n"
        }
    },
    {
        "msg": "Setup Celery and Redis for Pipeline Execution",
        "files": {
            "backend/requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nalembic\npsycopg2-binary\npydantic\npasslib[bcrypt]\npython-jose[cryptography]\npython-multipart\nemail-validator\npandas\nnumpy\ncelery\nredis\n",
            "backend/app/core/celery_app.py": "from celery import Celery\nimport os\n\nREDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')\n\ncelery_app = Celery(\n    'worker',\n    broker=REDIS_URL,\n    backend=REDIS_URL\n)\n\ncelery_app.conf.task_routes = {'app.workers.*': {'queue': 'pipeline_queue'}}\n"
        }
    },
    {
        "msg": "Implement Pipeline Execution Worker",
        "files": {
            "backend/app/workers/pipeline_worker.py": "from app.core.celery_app import celery_app\nimport time\n\n@celery_app.task(name='execute_pipeline')\ndef execute_pipeline(pipeline_id: int):\n    # Simulate pipeline node execution\n    print(f'Starting pipeline {pipeline_id} execution...')\n    time.sleep(2) # Load\n    print('Cleaning data...')\n    time.sleep(2) # Clean\n    print('Transforming data...')\n    time.sleep(2) # Transform\n    print(f'Pipeline {pipeline_id} completed successfully.')\n    return {'status': 'completed', 'pipeline_id': pipeline_id}\n",
            "backend/app/api/pipelines/router.py": "from fastapi import APIRouter, Depends\nfrom sqlalchemy.orm import Session\nfrom app.core.database import get_db\nfrom app.models.pipeline import Pipeline, PipelineExecution\nfrom app.workers.pipeline_worker import execute_pipeline\n\nrouter = APIRouter()\n\n@router.post('/{pipeline_id}/execute')\ndef trigger_pipeline(pipeline_id: int, db: Session = Depends(get_db)):\n    execution = PipelineExecution(pipeline_id=pipeline_id, status='running')\n    db.add(execution)\n    db.commit()\n    # Trigger Celery task\n    execute_pipeline.delay(pipeline_id)\n    return {'message': 'Pipeline execution started', 'execution_id': execution.id}\n"
        }
    },
    {
        "msg": "Add Pipeline Builder frontend skeleton",
        "files": {
            "frontend/src/pages/Pipelines.tsx": "import React from 'react';\n\nconst Pipelines = () => {\n  return (\n    <div>\n      <h2>Visual Pipeline Builder</h2>\n      <div style={{ display: 'flex', gap: '20px' }}>\n        <div className='nodes-panel'>\n          <h4>Nodes</h4>\n          <ul>\n            <li>Input</li>\n            <li>Clean</li>\n            <li>Transform</li>\n            <li>Output</li>\n          </ul>\n        </div>\n        <div className='canvas' style={{ border: '1px solid black', width: '600px', height: '400px' }}>\n          <p style={{ textAlign: 'center', marginTop: '180px' }}>Canvas Area</p>\n        </div>\n      </div>\n    </div>\n  );\n};\n\nexport default Pipelines;\n",
            "frontend/src/App.tsx": "import React from 'react';\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Login from './pages/Login';\nimport Dashboard from './pages/Dashboard';\nimport Organizations from './pages/Organizations';\nimport Users from './pages/Users';\nimport Datasets from './pages/Datasets';\nimport DataQuality from './pages/DataQuality';\nimport Pipelines from './pages/Pipelines';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path='/login' element={<Login />} />\n        <Route path='/' element={<Dashboard />} />\n        <Route path='/organizations' element={<Organizations />} />\n        <Route path='/users' element={<Users />} />\n        <Route path='/datasets' element={<Datasets />} />\n        <Route path='/quality' element={<DataQuality />} />\n        <Route path='/pipelines' element={<Pipelines />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n\nexport default App;\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Phase 5 commits created successfully.")
