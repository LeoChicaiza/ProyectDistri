from pydantic import BaseModel
from typing import Optional

class PlateValidationRequest(BaseModel):
    license_plate: str

class PlateValidationResponse(BaseModel):
    license_plate: str
    is_valid: bool
    reason: Optional[str] = None

