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
        "msg": "Add Dataset models and storage schemas",
        "files": {
            "backend/app/models/dataset.py": "from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON\nfrom sqlalchemy.orm import relationship\nfrom app.core.database import Base\n\nclass Dataset(Base):\n    __tablename__ = 'datasets'\n    id = Column(Integer, primary_key=True, index=True)\n    name = Column(String, index=True, nullable=False)\n    file_path = Column(String, nullable=False)\n    file_size_bytes = Column(Integer)\n    row_count = Column(Integer)\n    column_count = Column(Integer)\n    status = Column(String, default='pending')\n    organization_id = Column(Integer, ForeignKey('organizations.id'))\n    organization = relationship('Organization')\n    profile_data = Column(JSON, nullable=True)\n"
        }
    },
    {
        "msg": "Implement Dataset upload and storage logic",
        "files": {
            "backend/app/api/datasets/router.py": "from fastapi import APIRouter, Depends, UploadFile, File, HTTPException\nfrom sqlalchemy.orm import Session\nfrom app.core.database import get_db\nfrom app.models.dataset import Dataset\nimport os\nimport shutil\nimport uuid\n\nrouter = APIRouter()\nSTORAGE_PATH = os.getenv('STORAGE_PATH', './storage')\n\n@router.post('/upload')\ndef upload_dataset(file: UploadFile = File(...), db: Session = Depends(get_db)):\n    if not file.filename.endswith(('.csv', '.xlsx', '.json')):\n        raise HTTPException(status_code=400, detail='Invalid file type')\n    \n    os.makedirs(STORAGE_PATH, exist_ok=True)\n    file_id = str(uuid.uuid4())\n    file_path = os.path.join(STORAGE_PATH, f\"{file_id}_{file.filename}\")\n    \n    with open(file_path, 'wb') as buffer:\n        shutil.copyfileobj(file.file, buffer)\n        \n    dataset = Dataset(\n        name=file.filename,\n        file_path=file_path,\n        status='uploaded',\n        file_size_bytes=os.path.getsize(file_path)\n    )\n    db.add(dataset)\n    db.commit()\n    db.refresh(dataset)\n    return {'id': dataset.id, 'name': dataset.name, 'status': dataset.status}\n",
            "backend/requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nalembic\npsycopg2-binary\npydantic\npasslib[bcrypt]\npython-jose[cryptography]\npython-multipart\nemail-validator\npandas\nnumpy\n"
        }
    },
    {
        "msg": "Add Dataset profiling engine skeleton using Pandas",
        "files": {
            "backend/app/data_engine/profiler.py": "import pandas as pd\nimport json\n\ndef profile_dataset(file_path: str):\n    if file_path.endswith('.csv'):\n        df = pd.read_csv(file_path)\n    elif file_path.endswith('.xlsx'):\n        df = pd.read_excel(file_path)\n    else:\n        raise ValueError('Unsupported file format for profiling')\n        \n    profile = {\n        'row_count': len(df),\n        'column_count': len(df.columns),\n        'columns': []\n    }\n    \n    for col in df.columns:\n        col_data = df[col]\n        col_profile = {\n            'name': col,\n            'type': str(col_data.dtype),\n            'null_count': int(col_data.isnull().sum()),\n            'unique_count': int(col_data.nunique())\n        }\n        if pd.api.types.is_numeric_dtype(col_data):\n            col_profile.update({\n                'min': float(col_data.min()) if not pd.isna(col_data.min()) else None,\n                'max': float(col_data.max()) if not pd.isna(col_data.max()) else None,\n                'mean': float(col_data.mean()) if not pd.isna(col_data.mean()) else None\n            })\n        profile['columns'].append(col_profile)\n        \n    return profile\n"
        }
    },
    {
        "msg": "Add frontend Dataset upload and listing pages",
        "files": {
            "frontend/src/pages/Datasets.tsx": "import React, { useState } from 'react';\n\nconst Datasets = () => {\n  const [uploading, setUploading] = useState(false);\n  \n  const handleUpload = (e: React.ChangeEvent<HTMLInputElement>) => {\n    if (e.target.files && e.target.files.length > 0) {\n      setUploading(true);\n      // Mock upload delay\n      setTimeout(() => setUploading(false), 2000);\n    }\n  };\n\n  return (\n    <div>\n      <h2>Dataset Management</h2>\n      <input type='file' accept='.csv,.xlsx,.json' onChange={handleUpload} />\n      {uploading && <p>Uploading...</p>}\n      <table>\n        <thead>\n          <tr><th>Name</th><th>Rows</th><th>Size</th><th>Status</th></tr>\n        </thead>\n        <tbody>\n          <tr><td>sales_data.csv</td><td>10,000</td><td>2.5 MB</td><td>Profiled</td></tr>\n        </tbody>\n      </table>\n    </div>\n  );\n};\n\nexport default Datasets;\n",
            "frontend/src/App.tsx": "import React from 'react';\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Login from './pages/Login';\nimport Dashboard from './pages/Dashboard';\nimport Organizations from './pages/Organizations';\nimport Users from './pages/Users';\nimport Datasets from './pages/Datasets';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path='/login' element={<Login />} />\n        <Route path='/' element={<Dashboard />} />\n        <Route path='/organizations' element={<Organizations />} />\n        <Route path='/users' element={<Users />} />\n        <Route path='/datasets' element={<Datasets />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n\nexport default App;\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Phase 3 commits created successfully.")
