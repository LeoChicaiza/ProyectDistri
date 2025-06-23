
from pydantic import BaseModel
from datetime import datetime

class ReservationRequest(BaseModel):
    reservation_id: str
    plate: str
    reserved_at: datetime
    for_time: datetime

class ReservationResponse(ReservationRequest):
    pass
