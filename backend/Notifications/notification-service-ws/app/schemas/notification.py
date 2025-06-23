
from pydantic import BaseModel

class NotificationRequest(BaseModel):
    recipient: str
    message: str
    channel: str  # email, sms, push

class NotificationResponse(BaseModel):
    recipient: str
    channel: str
    status: str
