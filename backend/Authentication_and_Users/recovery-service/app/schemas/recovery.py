from pydantic import BaseModel
from datetime import datetime

class RecoveryRequestCreate(BaseModel):
    user_id: str
    token: str
    expires_at: datetime

class RecoveryRequestResponse(BaseModel):
    recovery_id: str
    user_id: str
    token: str
    expires_at: datetime
    used: bool
    requested_at: datetime

