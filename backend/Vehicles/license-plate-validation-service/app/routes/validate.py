from fastapi import APIRouter, HTTPException
from app.schemas.plate import PlateValidationRequest, PlateValidationResponse
from app.database.db import get_connection
import uuid
import re

router = APIRouter()

@router.post("/validate", response_model=PlateValidationResponse)
def validate_plate(data: PlateValidationRequest):
    plate = data.license_plate.upper().strip()

    # Validación básica de formato
    pattern = r"^[A-Z0-9\-]{6,8}$"
    if not re.match(pattern, plate):
        return PlateValidationResponse(
            license_plate=plate,
            is_valid=False,
            reason="Formato inválido de placa"
        )

    try:
        conn = get_connection()
        cur = conn.cursor()

        # Insertar validación
        cur.execute("""
            INSERT INTO license_plate_validations (validation_id, license_plate, is_valid, reason)
            VALUES (%s, %s, %s, %s)
        """, (
            str(uuid.uuid4()),
            plate,
            True,
            "Placa válida"
        ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return PlateValidationResponse(
        license_plate=plate,
        is_valid=True,
        reason="Placa válida"
    )
