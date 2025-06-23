from fastapi import APIRouter, HTTPException
from app.schemas.maintenance import MaintenanceCreate, MaintenanceResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=MaintenanceResponse)
def create_maintenance(record: MaintenanceCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        maintenance_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO slot_maintenance (maintenance_id, slot_id, maintenance_date, description, is_resolved)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING maintenance_id, slot_id, maintenance_date, description, is_resolved
        """, (
            maintenance_id,
            record.slot_id,
            record.maintenance_date,
            record.description,
            record.is_resolved
        ))
        result = cur.fetchone()
        conn.commit()
        return MaintenanceResponse(
            maintenance_id=result[0],
            slot_id=result[1],
            maintenance_date=result[2],
            description=result[3],
            is_resolved=result[4]
        )
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.get("/{slot_id}", response_model=list[MaintenanceResponse])
def get_maintenance_by_slot(slot_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT maintenance_id, slot_id, maintenance_date, description, is_resolved
            FROM slot_maintenance
            WHERE slot_id = %s
        """, (slot_id,))
        rows = cur.fetchall()
        return [
            MaintenanceResponse(
                maintenance_id=row[0],
                slot_id=row[1],
                maintenance_date=row[2],
                description=row[3],
                is_resolved=row[4]
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
