
from pydantic import BaseModel

class RateCreate(BaseModel):
    vehicle_type: str
    hourly_rate: float

class RateResponse(BaseModel):
    vehicle_type: str
    hourly_rate: float
