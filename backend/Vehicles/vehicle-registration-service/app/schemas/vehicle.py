from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleCreate(BaseModel):
    license_plate: str
    brand: str
    model: str
    color: Optional[str]
    type: Optional[str]
    owner_id: str

class VehicleResponse(BaseModel):
    vehicle_id: str
    license_plate: str
    brand: str
    model: str
    color: Optional[str]
    type: Optional[str]
    owner_id: str
    registered_at: Optional[datetime]

