from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth.router import router as auth_router
from app.api.organizations.router import router as org_router
from app.api.users.router import router as user_router
from app.api.datasets.router import router as dataset_router
from app.api.analytics.router import router as analytics_router
from app.api.pipelines.router import router as pipeline_router

app = FastAPI(title='Enterprise Data Platform API')

app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173', 'http://127.0.0.1:5173', 'http://localhost:5174'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(org_router, prefix="/api/v1/organizations", tags=["Organizations"])
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(dataset_router, prefix="/api/v1/datasets", tags=["Datasets"])
app.include_router(analytics_router, prefix="/api/v1/analytics", tags=["Analytics"])
app.include_router(pipeline_router, prefix="/api/v1/pipelines", tags=["Pipelines"])

@app.get('/')
def read_root():
    return {'status': 'ok'}
