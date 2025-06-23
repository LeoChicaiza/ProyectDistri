from fastapi import APIRouter, HTTPException
from app.schemas.level import LevelCreate, LevelResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=LevelResponse)
def create_level(level: LevelCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        level_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO levels (level_id, lot_id, name, level_number)
            VALUES (%s, %s, %s, %s)
            RETURNING level_id, lot_id, name, level_number
        """, (level_id, level.parking_lot, level.name, level.level_number))
        result = cur.fetchone()
        conn.commit()
        return LevelResponse(
            level_id=result[0],
            parking_lot=result[1],
            name=result[2],
            level_number=result[3]
        )
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.get("/{lot_id}", response_model=list[LevelResponse])
def get_levels_by_lot(lot_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT level_id, lot_id, name, level_number
            FROM levels
            WHERE lot_id = %s
        """, (lot_id,))
        rows = cur.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No levels found for this lot_id")
        return [
            LevelResponse(
                level_id=row[0],
                parking_lot=row[1],
                name=row[2],
                level_number=row[3]
            ) for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

