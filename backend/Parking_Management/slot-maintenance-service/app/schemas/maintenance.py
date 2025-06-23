from pydantic import BaseModel
from datetime import date
from typing import Optional

class MaintenanceCreate(BaseModel):
    slot_id: str
    maintenance_date: date
    description: Optional[str] = None
    is_resolved: Optional[bool] = False

class MaintenanceResponse(BaseModel):
    maintenance_id: str
    slot_id: str
    maintenance_date: date
    description: Optional[str]
    is_resolved: bool

