from pydantic import BaseModel
from datetime import datetime

class ParkingLotCreate(BaseModel):
    name: str
    address: str

class ParkingLotResponse(BaseModel):
    lot_id: str
    name: str
    address: str
    created_at: datetime

