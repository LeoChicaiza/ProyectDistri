from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleHistoryCreate(BaseModel):
    vehicle_id: str
    event_type: str
    event_description: Optional[str] = None

class VehicleHistoryResponse(BaseModel):
    history_id: str
    vehicle_id: str
    event_type: str
    event_description: Optional[str] = None
    occurred_at: Optional[datetime] = None

