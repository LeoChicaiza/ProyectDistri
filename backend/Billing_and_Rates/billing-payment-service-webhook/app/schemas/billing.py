
from pydantic import BaseModel
from datetime import datetime

class PaymentRequest(BaseModel):
    ticket_id: str
    plate: str
    amount: float
    paid_at: datetime

class PaymentReceipt(PaymentRequest):
    status: str
