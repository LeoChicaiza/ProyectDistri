from fastapi import APIRouter, HTTPException
from app.schemas.zone import ZoneCreate, ZoneResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=ZoneResponse)
def create_zone(zone: ZoneCreate):
    conn = get_connection()
    cur = conn.cursor()
    try:
        zone_id = str(uuid.uuid4())
        cur.execute("""
            INSERT INTO zones (zone_id, level_id, name)
            VALUES (%s, %s, %s)
            RETURNING zone_id, level_id, name
        """, (
            zone_id,
            zone.level_id,
            zone.name
        ))
        result = cur.fetchone()
        conn.commit()
        return ZoneResponse(zone_id=result[0], level_id=result[1], name=result[2])
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.get("/by-level/{level_id}", response_model=list[ZoneResponse])
def get_zones_by_level(level_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT zone_id, level_id, name
            FROM zones
            WHERE level_id = %s
        """, (level_id,))
        rows = cur.fetchall()
        return [
            ZoneResponse(zone_id=row[0], level_id=row[1], name=row[2])
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

