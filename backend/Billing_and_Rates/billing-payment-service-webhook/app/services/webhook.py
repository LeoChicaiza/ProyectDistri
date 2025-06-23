
import httpx
from app.schemas.billing import PaymentRequest

WEBHOOK_URL = "https://webhook.site/your-custom-url"  # reemplazar por endpoint real

async def send_webhook(payment: PaymentRequest):
    payload = {
        "event": "payment_received",
        "ticket_id": payment.ticket_id,
        "plate": payment.plate,
        "amount": payment.amount,
        "paid_at": payment.paid_at.isoformat()
    }
    try:
        async with httpx.AsyncClient() as client:
            await client.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Webhook failed: {e}")
