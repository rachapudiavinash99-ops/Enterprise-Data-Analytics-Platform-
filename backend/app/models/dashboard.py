from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base

class Dashboard(Base):
    __tablename__ = 'dashboards'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    widgets = relationship('Widget', back_populates='dashboard')

class Widget(Base):
    __tablename__ = 'widgets'
    id = Column(Integer, primary_key=True, index=True)
    dashboard_id = Column(Integer, ForeignKey('dashboards.id'))
    title = Column(String, nullable=False)
    widget_type = Column(String, nullable=False) # e.g., 'bar_chart', 'kpi'
    config = Column(JSON, nullable=False) # Analytics query config
    layout = Column(JSON, nullable=False) # x, y, w, h
    dashboard = relationship('Dashboard', back_populates='widgets')
