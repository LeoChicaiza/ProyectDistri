
from pydantic import BaseModel
from datetime import datetime

class CancellationRequest(BaseModel):
    reservation_id: str
    cancelled_at: datetime
    reason: str

class CancellationResponse(CancellationRequest):
    pass
