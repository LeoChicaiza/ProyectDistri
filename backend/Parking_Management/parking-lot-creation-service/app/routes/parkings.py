from fastapi import APIRouter, HTTPException
from app.schemas.parking import ParkingLotCreate, ParkingLotResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=ParkingLotResponse)
def create_parking_lot(parking_lot: ParkingLotCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        lot_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO parking_lots (lot_id, name, address)
            VALUES (%s, %s, %s)
            RETURNING lot_id, name, address, created_at
        """, (lot_id, parking_lot.name, parking_lot.address))
        result = cur.fetchone()
        conn.commit()
        return ParkingLotResponse(
            lot_id=result[0],
            name=result[1],
            address=result[2],
            created_at=result[3]
        )
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.get("/", response_model=list[ParkingLotResponse])
def get_parking_lots():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT lot_id, name, address, created_at
            FROM parking_lots
        """)
        rows = cur.fetchall()
        return [
            ParkingLotResponse(
                lot_id=row[0],
                name=row[1],
                address=row[2],
                created_at=row[3]
            ) for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

