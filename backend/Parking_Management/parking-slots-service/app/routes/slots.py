from fastapi import APIRouter, HTTPException
from app.schemas.slot import SlotCreate, SlotResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=SlotResponse)
def create_slot(slot: SlotCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        slot_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO parking_slots (slot_id, zone_id, slot_number, slot_type, is_reserved)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING slot_id, zone_id, slot_number, slot_type, is_reserved
        """, (slot_id, slot.zone_id, slot.slot_number, slot.slot_type, slot.is_reserved))
        result = cur.fetchone()
        conn.commit()
        return SlotResponse(
            slot_id=result[0],
            zone_id=result[1],
            slot_number=result[2],
            slot_type=result[3],
            is_reserved=result[4]
        )
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

@router.get("/", response_model=list[SlotResponse])
def get_slots():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT slot_id, zone_id, slot_number, slot_type, is_reserved
            FROM parking_slots
        """)
        rows = cur.fetchall()
        return [
            SlotResponse(
                slot_id=row[0],
                zone_id=row[1],
                slot_number=row[2],
                slot_type=row[3],
                is_reserved=row[4]
            ) for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

