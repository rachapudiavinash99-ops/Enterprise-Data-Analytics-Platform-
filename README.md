# Enterprise Data & Analytics Platform

Welcome to the complete Enterprise Data & Analytics Platform. This platform allows organizations to register users, upload datasets, build visual ETL pipelines, execute those pipelines via background workers, and construct advanced interactive analytics dashboards.

## Architecture
- **Backend**: Python 3.12, FastAPI, SQLAlchemy, Alembic, Celery, Pandas
- **Frontend**: React, TypeScript, Vite, Recharts
- **Database**: PostgreSQL (Primary Data), Redis (Message Broker for Celery)

## Features Implemented
- Multi-tenant Organization System
- RBAC (Role-Based Access Control) & JWT Authentication
- Dataset Management (Upload, Storage)
- Data Profiling Engine (Pandas-driven Null Checks, Aggregations)
- Data Quality & Cleaning Rules Engine
- Visual Pipeline Builder & Execution Engine (Celery Workers)
- Analytics Engine
- Dashboard Builder
- Reporting & Audit Logs

## Getting Started Locally (Docker)

1. Clone the repository.
2. Copy the environment variables:
   ```bash
   cp .env.example .env
   ```
3. Start the entire stack (Database, Redis, FastAPI Backend, Celery Worker):
   ```bash
   docker compose up --build
   ```
4. Access the API at `http://localhost:8000/docs` (Swagger UI).
5. (Optional) Run the frontend in a separate terminal:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Project Structure
- `/backend/app`: FastAPI application logic, endpoints, data engines.
- `/backend/app/models`: SQLAlchemy Database Models.
- `/backend/app/data_engine`: Pandas-based profiling and transformation logic.
- `/frontend/src`: React application components, pages, and layouts.
- `/tests`: Pytest integration tests.
