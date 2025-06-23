
from fastapi import APIRouter, HTTPException
from app.schemas.reservation import ReservationRequest, ReservationResponse
from app.database.db import reservation_db

router = APIRouter()

@router.post("/", response_model=ReservationResponse)
def create_reservation(res: ReservationRequest):
    if res.reservation_id in reservation_db:
        raise HTTPException(status_code=400, detail="Reservation ID already exists")
    reservation_db[res.reservation_id] = res.dict()
    return ReservationResponse(**res.dict())

@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: str):
    data = reservation_db.get(reservation_id)
    if not data:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return ReservationResponse(**data)
