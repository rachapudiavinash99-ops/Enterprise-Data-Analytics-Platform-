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
        "msg": "Finalize Docker and Environment Configurations",
        "files": {
            ".env.example": "DATABASE_URL=postgresql://postgres:postgres@db:5432/enterprise_db\nREDIS_URL=redis://redis:6379/0\nJWT_SECRET=super-secret-key-change-in-prod\nACCESS_TOKEN_EXPIRE_MINUTES=30\nSTORAGE_PATH=./storage\nFRONTEND_URL=http://localhost:3000\n",
            "docker-compose.yml": "version: '3.8'\nservices:\n  db:\n    image: postgres:15\n    environment:\n      POSTGRES_USER: postgres\n      POSTGRES_PASSWORD: postgres\n      POSTGRES_DB: enterprise_db\n    ports:\n      - \"5432:5432\"\n    volumes:\n      - postgres_data:/var/lib/postgresql/data\n  \n  redis:\n    image: redis:7\n    ports:\n      - \"6379:6379\"\n\n  backend:\n    build:\n      context: .\n      dockerfile: Dockerfile\n    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload\n    volumes:\n      - ./backend/app:/app/app\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=postgresql://postgres:postgres@db:5432/enterprise_db\n      - REDIS_URL=redis://redis:6379/0\n    depends_on:\n      - db\n      - redis\n\n  worker:\n    build:\n      context: .\n      dockerfile: Dockerfile\n    command: celery -A app.core.celery_app worker --loglevel=info -Q pipeline_queue\n    volumes:\n      - ./backend/app:/app/app\n    environment:\n      - DATABASE_URL=postgresql://postgres:postgres@db:5432/enterprise_db\n      - REDIS_URL=redis://redis:6379/0\n    depends_on:\n      - db\n      - redis\n\nvolumes:\n  postgres_data:\n"
        }
    },
    {
        "msg": "Add Comprehensive README documentation",
        "files": {
            "README.md": "# Enterprise Data & Analytics Platform\n\nWelcome to the complete Enterprise Data & Analytics Platform. This platform allows organizations to register users, upload datasets, build visual ETL pipelines, execute those pipelines via background workers, and construct advanced interactive analytics dashboards.\n\n## Architecture\n- **Backend**: Python 3.12, FastAPI, SQLAlchemy, Alembic, Celery, Pandas\n- **Frontend**: React, TypeScript, Vite, Recharts\n- **Database**: PostgreSQL (Primary Data), Redis (Message Broker for Celery)\n\n## Features Implemented\n- Multi-tenant Organization System\n- RBAC (Role-Based Access Control) & JWT Authentication\n- Dataset Management (Upload, Storage)\n- Data Profiling Engine (Pandas-driven Null Checks, Aggregations)\n- Data Quality & Cleaning Rules Engine\n- Visual Pipeline Builder & Execution Engine (Celery Workers)\n- Analytics Engine\n- Dashboard Builder\n- Reporting & Audit Logs\n\n## Getting Started Locally (Docker)\n\n1. Clone the repository.\n2. Copy the environment variables:\n   ```bash\n   cp .env.example .env\n   ```\n3. Start the entire stack (Database, Redis, FastAPI Backend, Celery Worker):\n   ```bash\n   docker compose up --build\n   ```\n4. Access the API at `http://localhost:8000/docs` (Swagger UI).\n5. (Optional) Run the frontend in a separate terminal:\n   ```bash\n   cd frontend\n   npm install\n   npm run dev\n   ```\n\n## Project Structure\n- `/backend/app`: FastAPI application logic, endpoints, data engines.\n- `/backend/app/models`: SQLAlchemy Database Models.\n- `/backend/app/data_engine`: Pandas-based profiling and transformation logic.\n- `/frontend/src`: React application components, pages, and layouts.\n- `/tests`: Pytest integration tests.\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(0.5)

print("Final configuration commits created successfully.")
