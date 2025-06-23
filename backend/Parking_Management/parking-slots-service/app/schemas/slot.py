from pydantic import BaseModel
from typing import Optional

class SlotCreate(BaseModel):
    zone_id: str
    slot_number: str
    slot_type: str
    is_reserved: Optional[bool] = False

class SlotResponse(BaseModel):
    slot_id: str
    zone_id: str
    slot_number: str
    slot_type: str
    is_reserved: bool
