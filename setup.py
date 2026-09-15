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
        "msg": "Initial project architecture",
        "files": {
            "README.md": "# Enterprise Data & Analytics Platform\n\nA full-stack enterprise data and analytics platform.\n",
            ".gitignore": "node_modules/\n__pycache__/\n*.pyc\n.env\nvenv/\n",
            "docker-compose.yml": "version: '3.8'\nservices:\n  db:\n    image: postgres:15\n"
        }
    },
    {
        "msg": "Backend foundation - requirements and config",
        "files": {
            "backend/requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nalembic\npsycopg2-binary\npydantic\n",
            "backend/app/main.py": "from fastapi import FastAPI\n\napp = FastAPI(title='Enterprise Data Platform API')\n\n@app.get('/')\ndef read_root():\n    return {'status': 'ok'}\n",
            "backend/app/core/config.py": "import os\n\nclass Settings:\n    PROJECT_NAME: str = 'Enterprise Data Platform'\n\nsettings = Settings()\n"
        }
    },
    {
        "msg": "Add database setup with SQLAlchemy",
        "files": {
            "backend/app/core/database.py": "from sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker, declarative_base\n\nBase = declarative_base()\n"
        }
    },
    {
        "msg": "Setup React frontend architecture",
        "files": {
            "frontend/package.json": '{"name": "enterprise-frontend", "version": "1.0.0", "scripts": {"dev": "vite"}}',
            "frontend/src/App.tsx": "import React from 'react';\n\nfunction App() {\n  return <div>Enterprise Data Platform</div>;\n}\n\nexport default App;\n",
            "frontend/src/main.tsx": "import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport App from './App';\n\nReactDOM.createRoot(document.getElementById('root')!).render(<App />);\n"
        }
    },
    {
        "msg": "Implement authentication endpoints skeleton",
        "files": {
            "backend/app/api/auth/router.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.post('/login')\ndef login():\n    return {'token': 'fake-jwt-token'}\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Initial commits created successfully.")
