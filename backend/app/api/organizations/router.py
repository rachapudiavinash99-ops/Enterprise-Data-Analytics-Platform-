from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationResponse

router = APIRouter()

@router.post('/', response_model=OrganizationResponse)
def create_organization(org_in: OrganizationCreate, db: Session = Depends(get_db)):
    org = Organization(name=org_in.name)
    db.add(org)
    db.commit()
    db.refresh(org)
    return org

@router.get('/', response_model=list[OrganizationResponse])
def list_organizations(db: Session = Depends(get_db)):
    return db.query(Organization).all()
