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
        "msg": "Deep Implementation: Enhance Dataset Profiler with detailed metrics",
        "files": {
            "backend/app/data_engine/profiler.py": "import pandas as pd\nimport json\nimport numpy as np\n\ndef profile_dataset(file_path: str):\n    try:\n        if file_path.endswith('.csv'):\n            df = pd.read_csv(file_path)\n        elif file_path.endswith('.xlsx'):\n            df = pd.read_excel(file_path)\n        else:\n            raise ValueError('Unsupported file format')\n            \n        profile = {\n            'row_count': len(df),\n            'column_count': len(df.columns),\n            'columns': []\n        }\n        \n        for col in df.columns:\n            col_data = df[col]\n            col_profile = {\n                'name': col,\n                'type': str(col_data.dtype),\n                'null_count': int(col_data.isnull().sum()),\n                'null_percentage': float((col_data.isnull().sum() / len(df)) * 100) if len(df) > 0 else 0,\n                'unique_count': int(col_data.nunique())\n            }\n            \n            if pd.api.types.is_numeric_dtype(col_data):\n                col_profile.update({\n                    'min': float(col_data.min()) if not pd.isna(col_data.min()) else None,\n                    'max': float(col_data.max()) if not pd.isna(col_data.max()) else None,\n                    'mean': float(col_data.mean()) if not pd.isna(col_data.mean()) else None,\n                    'median': float(col_data.median()) if not pd.isna(col_data.median()) else None,\n                    'std_dev': float(col_data.std()) if not pd.isna(col_data.std()) else None,\n                })\n            elif pd.api.types.is_string_dtype(col_data):\n                top_values = col_data.value_counts().head(5).to_dict()\n                col_profile['top_values'] = {str(k): int(v) for k, v in top_values.items()}\n                \n            profile['columns'].append(col_profile)\n            \n        return profile\n    except Exception as e:\n        return {'error': str(e)}\n"
        }
    },
    {
        "msg": "Deep Implementation: Integrate Profiler in Dataset Upload Route",
        "files": {
            "backend/app/api/datasets/router.py": "from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks, HTTPException\nfrom sqlalchemy.orm import Session\nfrom app.core.database import get_db\nfrom app.models.dataset import Dataset\nfrom app.data_engine.profiler import profile_dataset\nimport os\nimport shutil\nimport uuid\n\nrouter = APIRouter()\nSTORAGE_PATH = os.getenv('STORAGE_PATH', './storage')\n\ndef process_and_profile_dataset(dataset_id: int, file_path: str, db: Session):\n    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()\n    if not dataset:\n        return\n    \n    try:\n        profile = profile_dataset(file_path)\n        dataset.profile_data = profile\n        if 'error' in profile:\n            dataset.status = 'failed'\n        else:\n            dataset.status = 'profiled'\n            dataset.row_count = profile.get('row_count', 0)\n            dataset.column_count = profile.get('column_count', 0)\n        db.commit()\n    except Exception as e:\n        dataset.status = 'failed'\n        db.commit()\n\n@router.post('/upload')\ndef upload_dataset(background_tasks: BackgroundTasks, file: UploadFile = File(...), db: Session = Depends(get_db)):\n    if not file.filename.endswith(('.csv', '.xlsx', '.json')):\n        raise HTTPException(status_code=400, detail='Invalid file type')\n    \n    os.makedirs(STORAGE_PATH, exist_ok=True)\n    file_id = str(uuid.uuid4())\n    file_path = os.path.join(STORAGE_PATH, f\"{file_id}_{file.filename}\")\n    \n    with open(file_path, 'wb') as buffer:\n        shutil.copyfileobj(file.file, buffer)\n        \n    dataset = Dataset(\n        name=file.filename,\n        file_path=file_path,\n        status='uploaded',\n        file_size_bytes=os.path.getsize(file_path)\n    )\n    db.add(dataset)\n    db.commit()\n    db.refresh(dataset)\n    \n    background_tasks.add_task(process_and_profile_dataset, dataset.id, file_path, db)\n    \n    return {'id': dataset.id, 'name': dataset.name, 'status': 'processing'}\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(0.5)

print("Deep implementation commits created successfully.")
