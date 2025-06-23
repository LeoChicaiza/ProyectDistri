
from pydantic import BaseModel
from datetime import datetime

class TicketRequest(BaseModel):
    ticket_id: str
    plate: str
    issued_at: datetime
    amount: float

class TicketResponse(BaseModel):
    ticket_id: str
    plate: str
    issued_at: datetime
    amount: float
