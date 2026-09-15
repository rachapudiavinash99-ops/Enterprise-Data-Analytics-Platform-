from pydantic import BaseModel
from typing import List, Optional

class OrganizationBase(BaseModel):
    name: str

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationResponse(OrganizationBase):
    id: int

    class Config:
        orm_mode = True
