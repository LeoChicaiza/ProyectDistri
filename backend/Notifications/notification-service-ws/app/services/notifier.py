
from app.schemas.notification import NotificationRequest
from app.services.manager import connection_manager

async def send_notification(request: NotificationRequest) -> str:
    msg = f"[{request.channel.upper()}] To: {request.recipient} — {request.message}"
    await connection_manager.broadcast(msg)
    return "sent"
