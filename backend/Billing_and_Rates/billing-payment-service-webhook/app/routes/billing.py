
from fastapi import APIRouter, HTTPException
from app.schemas.billing import PaymentRequest, PaymentReceipt
from app.database.db import billing_db
from app.services.webhook import send_webhook
import asyncio

router = APIRouter()

@router.post("/pay", response_model=PaymentReceipt)
async def process_payment(payment: PaymentRequest):
    if payment.ticket_id in billing_db:
        raise HTTPException(status_code=400, detail="Payment already processed")
    billing_db[payment.ticket_id] = payment.dict()
    asyncio.create_task(send_webhook(payment))  # enviar hook en segundo plano
    return PaymentReceipt(**payment.dict(), status="paid")

@router.get("/status/{ticket_id}", response_model=PaymentReceipt)
def get_payment_status(ticket_id: str):
    data = billing_db.get(ticket_id)
    if not data:
        raise HTTPException(status_code=404, detail="No payment found for this ticket")
    return PaymentReceipt(**data, status="paid")
