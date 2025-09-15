from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class Dataset(Base):
    __tablename__ = 'datasets'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    file_path = Column(String, nullable=False)
    file_size_bytes = Column(Integer)
    row_count = Column(Integer)
    column_count = Column(Integer)
    status = Column(String, default='pending')
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization = relationship('Organization')
    profile_data = Column(JSON, nullable=True)
