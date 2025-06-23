from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserProfileCreate(BaseModel):
    user_id: str
    full_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]

class UserProfileResponse(BaseModel):
    profile_id: str
    user_id: str
    full_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    created_at: datetime

