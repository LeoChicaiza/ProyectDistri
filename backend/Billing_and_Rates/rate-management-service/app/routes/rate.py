
from fastapi import APIRouter, HTTPException
from app.schemas.rate import RateCreate, RateResponse
from app.database.db import rates_db

router = APIRouter()

@router.post("/", response_model=RateResponse)
def create_rate(rate: RateCreate):
    if rate.vehicle_type in rates_db:
        raise HTTPException(status_code=400, detail="Rate already defined for this vehicle type")
    rates_db[rate.vehicle_type] = rate.dict()
    return RateResponse(**rate.dict())

@router.get("/{vehicle_type}", response_model=RateResponse)
def get_rate(vehicle_type: str):
    rate = rates_db.get(vehicle_type)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    return RateResponse(**rate)
