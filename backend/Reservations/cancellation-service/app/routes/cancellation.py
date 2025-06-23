
from fastapi import APIRouter, HTTPException
from app.schemas.cancellation import CancellationRequest, CancellationResponse
from app.database.db import cancellation_db

router = APIRouter()

@router.post("/", response_model=CancellationResponse)
def cancel_reservation(data: CancellationRequest):
    if data.reservation_id in cancellation_db:
        raise HTTPException(status_code=400, detail="Reservation already cancelled")
    cancellation_db[data.reservation_id] = data.dict()
    return CancellationResponse(**data.dict())

@router.get("/{reservation_id}", response_model=CancellationResponse)
def get_cancellation(reservation_id: str):
    data = cancellation_db.get(reservation_id)
    if not data:
        raise HTTPException(status_code=404, detail="Cancellation not found")
    return CancellationResponse(**data)
