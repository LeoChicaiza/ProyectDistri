from fastapi import APIRouter, HTTPException
from app.schemas.history import VehicleHistoryCreate, VehicleHistoryResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=VehicleHistoryResponse)
def add_history_entry(entry: VehicleHistoryCreate):
    conn = get_connection()
    cursor = conn.cursor()
    history_id = str(uuid.uuid4())
    
    try:
        cursor.execute("""
            INSERT INTO vehicle_history (history_id, vehicle_id, event_type, event_description)
            VALUES (%s, %s, %s, %s)
        """, (history_id, entry.vehicle_id, entry.event_type, entry.event_description))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    
    return VehicleHistoryResponse(
        history_id=history_id,
        vehicle_id=entry.vehicle_id,
        event_type=entry.event_type,
        event_description=entry.event_description
    )


@router.get("/{vehicle_id}", response_model=list[VehicleHistoryResponse])
def get_vehicle_history(vehicle_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT history_id, vehicle_id, event_type, event_description, occurred_at
            FROM vehicle_history
            WHERE vehicle_id = %s
            ORDER BY occurred_at DESC
        """, (vehicle_id,))
        rows = cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

    return [VehicleHistoryResponse(
        history_id=row[0],
        vehicle_id=row[1],
        event_type=row[2],
        event_description=row[3],
        occurred_at=row[4]
    ) for row in rows]

