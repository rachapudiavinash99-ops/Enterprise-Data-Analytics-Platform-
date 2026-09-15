from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from app.core.database import Base

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    config = Column(JSON, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
