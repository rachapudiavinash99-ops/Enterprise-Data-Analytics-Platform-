from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    status = Column(String, default='open')
