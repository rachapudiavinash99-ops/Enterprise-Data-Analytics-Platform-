from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Pipeline(Base):
    __tablename__ = 'pipelines'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    nodes = Column(JSON, nullable=False) # Visual pipeline graph nodes
    edges = Column(JSON, nullable=False) # Visual pipeline graph edges
    organization_id = Column(Integer, ForeignKey('organizations.id'))

class PipelineExecution(Base):
    __tablename__ = 'pipeline_executions'
    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey('pipelines.id'))
    status = Column(String, default='pending')
    logs = Column(JSON)
