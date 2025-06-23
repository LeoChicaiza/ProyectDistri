
from fastapi import APIRouter, HTTPException
from app.schemas.availability import SlotAvailability, AvailabilityResponse
from app.database.db import get_connection
import psycopg2

router = APIRouter()

@router.post("/update", response_model=AvailabilityResponse)
def update_availability(status: SlotAvailability):
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        # Verificar si el registro ya existe
        cur.execute("SELECT availability_id FROM slot_availability WHERE slot_id = %s", (status.slot_id,))
        result = cur.fetchone()

        if result:
            cur.execute(
                "UPDATE slot_availability SET is_available = %s, last_checked = CURRENT_TIMESTAMP WHERE slot_id = %s",
                (status.status, status.slot_id)
            )
        else:
            availability_id = f"av-{status.slot_id}"
            cur.execute(
                "INSERT INTO slot_availability (availability_id, slot_id, is_available) VALUES (%s, %s, %s)",
                (availability_id, status.slot_id, status.status)
            )

        conn.commit()
        cur.close()
        conn.close()
        return AvailabilityResponse(slot_id=status.slot_id, status=status.status)
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{slot_id}", response_model=AvailabilityResponse)
def get_availability(slot_id: str):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT is_available FROM slot_availability WHERE slot_id = %s", (slot_id,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            return AvailabilityResponse(slot_id=slot_id, status=result[0])
        else:
            raise HTTPException(status_code=404, detail="Slot not found")
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

