from pydantic import BaseModel
from datetime import datetime

class SessionCreate(BaseModel):
    user_id: str
    ip_address: str
    user_agent: str

class SessionResponse(BaseModel):
    session_id: str
    user_id: str
    ip_address: str
    user_agent: str
    login_time: datetime
    is_active: bool

