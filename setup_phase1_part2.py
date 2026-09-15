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
        "msg": "Add SQLAlchemy User model and Pydantic schemas",
        "files": {
            "backend/app/models/user.py": "from sqlalchemy import Column, Integer, String, Boolean\nfrom app.core.database import Base\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True, index=True)\n    email = Column(String, unique=True, index=True, nullable=False)\n    hashed_password = Column(String, nullable=False)\n    is_active = Column(Boolean, default=True)\n    is_superuser = Column(Boolean, default=False)\n",
            "backend/app/schemas/user.py": "from pydantic import BaseModel, EmailStr\nfrom typing import Optional\n\nclass UserCreate(BaseModel):\n    email: EmailStr\n    password: str\n\nclass UserResponse(BaseModel):\n    id: int\n    email: EmailStr\n    is_active: bool\n\n    class Config:\n        orm_mode = True\n"
        }
    },
    {
        "msg": "Implement security utilities (Password Hashing & JWT)",
        "files": {
            "backend/requirements.txt": "fastapi\nuvicorn\nsqlalchemy\nalembic\npsycopg2-binary\npydantic\npasslib[bcrypt]\npython-jose[cryptography]\npython-multipart\nemail-validator\n",
            "backend/app/core/security.py": "from passlib.context import CryptContext\nfrom jose import jwt\nfrom datetime import datetime, timedelta\nimport os\n\npwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')\nSECRET_KEY = os.getenv('JWT_SECRET', 'supersecretkey')\nALGORITHM = 'HS256'\nACCESS_TOKEN_EXPIRE_MINUTES = 30\n\ndef verify_password(plain_password, hashed_password):\n    return pwd_context.verify(plain_password, hashed_password)\n\ndef get_password_hash(password):\n    return pwd_context.hash(password)\n\ndef create_access_token(data: dict):\n    to_encode = data.copy()\n    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)\n    to_encode.update({'exp': expire})\n    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)\n"
        }
    },
    {
        "msg": "Implement Authentication router (Register & Login)",
        "files": {
            "backend/app/api/auth/router.py": "from fastapi import APIRouter, Depends, HTTPException, status\nfrom sqlalchemy.orm import Session\nfrom fastapi.security import OAuth2PasswordRequestForm\nfrom app.core.database import get_db\nfrom app.models.user import User\nfrom app.schemas.user import UserCreate, UserResponse\nfrom app.core.security import get_password_hash, verify_password, create_access_token\n\nrouter = APIRouter()\n\n@router.post('/register', response_model=UserResponse)\ndef register(user_in: UserCreate, db: Session = Depends(get_db)):\n    user = db.query(User).filter(User.email == user_in.email).first()\n    if user:\n        raise HTTPException(status_code=400, detail='Email already registered')\n    hashed_password = get_password_hash(user_in.password)\n    new_user = User(email=user_in.email, hashed_password=hashed_password)\n    db.add(new_user)\n    db.commit()\n    db.refresh(new_user)\n    return new_user\n\n@router.post('/login')\ndef login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):\n    user = db.query(User).filter(User.email == form_data.username).first()\n    if not user or not verify_password(form_data.password, user.hashed_password):\n        raise HTTPException(status_code=400, detail='Incorrect email or password')\n    access_token = create_access_token(data={'sub': user.email})\n    return {'access_token': access_token, 'token_type': 'bearer'}\n",
            "backend/app/core/database.py": "from sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker, declarative_base\nimport os\n\nDATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/enterprise_db')\nengine = create_engine(DATABASE_URL)\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\nBase = declarative_base()\n\ndef get_db():\n    db = SessionLocal()\n    try:\n        yield db\n    finally:\n        db.close()\n"
        }
    },
    {
        "msg": "Setup Alembic for database migrations",
        "files": {
            "backend/alembic.ini": "[alembic]\nscript_location = alembic\nsqlalchemy.url = postgresql://postgres:postgres@localhost:5432/enterprise_db\n",
            "backend/alembic/env.py": "from logging.config import fileConfig\nfrom sqlalchemy import engine_from_config\nfrom sqlalchemy import pool\nfrom alembic import context\nfrom app.core.database import Base\nfrom app.models.user import User\n\nconfig = context.config\nif config.config_file_name is not None:\n    fileConfig(config.config_file_name)\ntarget_metadata = Base.metadata\n\ndef run_migrations_offline() -> None:\n    url = config.get_main_option('sqlalchemy.url')\n    context.configure(\n        url=url,\n        target_metadata=target_metadata,\n        literal_binds=True,\n        dialect_opts={'paramstyle': 'named'},\n    )\n    with context.begin_transaction():\n        context.run_migrations()\n\ndef run_migrations_online() -> None:\n    connectable = engine_from_config(\n        config.get_section(config.config_ini_section, {}),\n        prefix='sqlalchemy.',\n        poolclass=pool.NullPool,\n    )\n    with connectable.connect() as connection:\n        context.configure(\n            connection=connection, target_metadata=target_metadata\n        )\n        with context.begin_transaction():\n            context.run_migrations()\n\nif context.is_offline_mode():\n    run_migrations_offline()\nelse:\n    run_migrations_online()\n"
        }
    },
    {
        "msg": "Add frontend routing and Login skeleton",
        "files": {
            "frontend/package.json": '{"name": "enterprise-frontend", "version": "1.0.0", "scripts": {"dev": "vite"}, "dependencies": {"react-router-dom": "^6.20.0", "axios": "^1.6.0"}}',
            "frontend/src/App.tsx": "import React from 'react';\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Login from './pages/Login';\nimport Dashboard from './pages/Dashboard';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path='/login' element={<Login />} />\n        <Route path='/' element={<Dashboard />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n\nexport default App;\n",
            "frontend/src/pages/Login.tsx": "import React from 'react';\n\nconst Login = () => {\n  return (\n    <div className='login-container'>\n      <h2>Enterprise Login</h2>\n      <form>\n        <input type='email' placeholder='Email' />\n        <input type='password' placeholder='Password' />\n        <button type='submit'>Sign In</button>\n      </form>\n    </div>\n  );\n};\n\nexport default Login;\n",
            "frontend/src/pages/Dashboard.tsx": "import React from 'react';\n\nconst Dashboard = () => {\n  return (\n    <div>\n      <h1>Analytics Dashboard</h1>\n      <p>Welcome to the Enterprise Data Platform</p>\n    </div>\n  );\n};\n\nexport default Dashboard;\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Phase 1 Part 2 commits created successfully.")
