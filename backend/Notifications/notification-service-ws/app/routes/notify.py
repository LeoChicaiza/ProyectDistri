
from fastapi import APIRouter
from app.schemas.notification import NotificationRequest, NotificationResponse
from app.services.notifier import send_notification

router = APIRouter()

@router.post("/", response_model=NotificationResponse)
async def notify(request: NotificationRequest):
    status = await send_notification(request)
    return NotificationResponse(recipient=request.recipient, channel=request.channel, status=status)
