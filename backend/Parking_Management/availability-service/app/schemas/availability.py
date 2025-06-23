
from pydantic import BaseModel

class SlotAvailability(BaseModel):
    parking_lot: str
    level: int
    zone: str
    slot_id: str
    status: str  

class AvailabilityResponse(BaseModel):
    slot_id: str
    status: str
