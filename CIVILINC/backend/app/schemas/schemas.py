from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.models import ProjectStatus, ComplaintStatus

# Project Schemas
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    budget: Optional[float] = None
    status: ProjectStatus = ProjectStatus.PLANNED
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    budget: Optional[float] = None
    status: Optional[ProjectStatus] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class Project(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Complaint Schemas
class ComplaintBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    status: ComplaintStatus = ComplaintStatus.PENDING
    project_id: Optional[int] = None

class ComplaintCreate(ComplaintBase):
    pass

class ComplaintUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    status: Optional[ComplaintStatus] = None
    project_id: Optional[int] = None

class Complaint(ComplaintBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# City Service Schemas
class CityServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    department: str
    contact_number: str
    email: str
    location: str

class CityServiceCreate(CityServiceBase):
    pass

class CityServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    department: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    location: Optional[str] = None

class CityService(CityServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Local Event Schemas
class LocalEventBase(BaseModel):
    title: str
    description: Optional[str] = None
    event_date: datetime
    location: str
    organizer: str
    contact_number: str

class LocalEventCreate(LocalEventBase):
    pass

class LocalEventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    event_date: Optional[datetime] = None
    location: Optional[str] = None
    organizer: Optional[str] = None
    contact_number: Optional[str] = None

class LocalEvent(LocalEventBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 