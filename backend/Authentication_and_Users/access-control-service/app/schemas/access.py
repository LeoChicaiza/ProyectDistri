from pydantic import BaseModel
from datetime import datetime

class AccessControlCreate(BaseModel):
    user_id: str
    resource: str
    permission_level: str

class AccessControlResponse(BaseModel):
    access_id: str
    user_id: str
    resource: str
    permission_level: str
    granted_at: datetime

