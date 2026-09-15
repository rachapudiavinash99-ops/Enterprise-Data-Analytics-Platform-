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
        "msg": "Add Organization and Role models for multi-tenancy",
        "files": {
            "backend/app/models/organization.py": "from sqlalchemy import Column, Integer, String\nfrom sqlalchemy.orm import relationship\nfrom app.core.database import Base\n\nclass Organization(Base):\n    __tablename__ = 'organizations'\n    id = Column(Integer, primary_key=True, index=True)\n    name = Column(String, unique=True, index=True, nullable=False)\n    users = relationship('User', back_populates='organization')\n",
            "backend/app/models/role.py": "from sqlalchemy import Column, Integer, String, Table, ForeignKey\nfrom sqlalchemy.orm import relationship\nfrom app.core.database import Base\n\nrole_permissions = Table(\n    'role_permissions',\n    Base.metadata,\n    Column('role_id', Integer, ForeignKey('roles.id')),\n    Column('permission_id', Integer, ForeignKey('permissions.id'))\n)\n\nclass Role(Base):\n    __tablename__ = 'roles'\n    id = Column(Integer, primary_key=True, index=True)\n    name = Column(String, unique=True, nullable=False)\n    permissions = relationship('Permission', secondary=role_permissions)\n\nclass Permission(Base):\n    __tablename__ = 'permissions'\n    id = Column(Integer, primary_key=True, index=True)\n    name = Column(String, unique=True, nullable=False)\n"
        }
    },
    {
        "msg": "Update User model with relationships",
        "files": {
            "backend/app/models/user.py": "from sqlalchemy import Column, Integer, String, Boolean, ForeignKey\nfrom sqlalchemy.orm import relationship\nfrom app.core.database import Base\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True, index=True)\n    email = Column(String, unique=True, index=True, nullable=False)\n    hashed_password = Column(String, nullable=False)\n    is_active = Column(Boolean, default=True)\n    is_superuser = Column(Boolean, default=False)\n    organization_id = Column(Integer, ForeignKey('organizations.id'))\n    organization = relationship('Organization', back_populates='users')\n"
        }
    },
    {
        "msg": "Add schemas for Organizations and Roles",
        "files": {
            "backend/app/schemas/organization.py": "from pydantic import BaseModel\nfrom typing import List, Optional\n\nclass OrganizationBase(BaseModel):\n    name: str\n\nclass OrganizationCreate(OrganizationBase):\n    pass\n\nclass OrganizationResponse(OrganizationBase):\n    id: int\n\n    class Config:\n        orm_mode = True\n"
        }
    },
    {
        "msg": "Implement Organization and User routers",
        "files": {
            "backend/app/api/organizations/router.py": "from fastapi import APIRouter, Depends, HTTPException\nfrom sqlalchemy.orm import Session\nfrom app.core.database import get_db\nfrom app.models.organization import Organization\nfrom app.schemas.organization import OrganizationCreate, OrganizationResponse\n\nrouter = APIRouter()\n\n@router.post('/', response_model=OrganizationResponse)\ndef create_organization(org_in: OrganizationCreate, db: Session = Depends(get_db)):\n    org = Organization(name=org_in.name)\n    db.add(org)\n    db.commit()\n    db.refresh(org)\n    return org\n\n@router.get('/', response_model=list[OrganizationResponse])\ndef list_organizations(db: Session = Depends(get_db)):\n    return db.query(Organization).all()\n",
            "backend/app/api/users/router.py": "from fastapi import APIRouter, Depends\nfrom sqlalchemy.orm import Session\nfrom app.core.database import get_db\nfrom app.models.user import User\nfrom app.schemas.user import UserResponse\n\nrouter = APIRouter()\n\n@router.get('/', response_model=list[UserResponse])\ndef list_users(db: Session = Depends(get_db)):\n    return db.query(User).all()\n"
        }
    },
    {
        "msg": "Add frontend pages for Users and Organizations",
        "files": {
            "frontend/src/pages/Organizations.tsx": "import React from 'react';\n\nconst Organizations = () => {\n  return (\n    <div>\n      <h2>Organization Management</h2>\n      <button>Create Organization</button>\n      <table>\n        <thead>\n          <tr><th>ID</th><th>Name</th></tr>\n        </thead>\n        <tbody>\n          <tr><td>1</td><td>Demo Org</td></tr>\n        </tbody>\n      </table>\n    </div>\n  );\n};\n\nexport default Organizations;\n",
            "frontend/src/pages/Users.tsx": "import React from 'react';\n\nconst Users = () => {\n  return (\n    <div>\n      <h2>User Management</h2>\n      <button>Invite User</button>\n      <table>\n        <thead>\n          <tr><th>Email</th><th>Role</th><th>Status</th></tr>\n        </thead>\n        <tbody>\n          <tr><td>admin@demo.com</td><td>Admin</td><td>Active</td></tr>\n        </tbody>\n      </table>\n    </div>\n  );\n};\n\nexport default Users;\n",
            "frontend/src/App.tsx": "import React from 'react';\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Login from './pages/Login';\nimport Dashboard from './pages/Dashboard';\nimport Organizations from './pages/Organizations';\nimport Users from './pages/Users';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path='/login' element={<Login />} />\n        <Route path='/' element={<Dashboard />} />\n        <Route path='/organizations' element={<Organizations />} />\n        <Route path='/users' element={<Users />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n\nexport default App;\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Phase 2 commits created successfully.")
