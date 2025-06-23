
from fastapi import APIRouter
from datetime import datetime
from app.schemas.calc import CalculationRequest, CalculationResponse

router = APIRouter()

@router.post("/", response_model=CalculationResponse)
def calculate_payment(data: CalculationRequest):
    duration = (data.exit_time - data.entry_time).total_seconds() / 3600
    duration = max(1, int(duration + 0.99))  # redondeo hacia arriba
    total = duration * data.hourly_rate
    return CalculationResponse(
        plate=data.plate,
        hours_charged=duration,
        total_amount=round(total, 2)
    )
