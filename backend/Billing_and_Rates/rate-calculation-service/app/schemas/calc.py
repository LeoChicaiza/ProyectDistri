
from pydantic import BaseModel
from datetime import datetime

class CalculationRequest(BaseModel):
    plate: str
    entry_time: datetime
    exit_time: datetime
    hourly_rate: float

class CalculationResponse(BaseModel):
    plate: str
    hours_charged: int
    total_amount: float
