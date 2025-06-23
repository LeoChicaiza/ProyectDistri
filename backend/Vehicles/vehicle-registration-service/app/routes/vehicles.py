from fastapi import APIRouter, HTTPException
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/", response_model=VehicleResponse)
def register_vehicle(data: VehicleCreate):
    conn = get_connection()
    cursor = conn.cursor()
    vehicle_id = str(uuid.uuid4())
    
    try:
        cursor.execute("""
            INSERT INTO vehicles (vehicle_id, license_plate, brand, model, color, type, owner_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            vehicle_id,
            data.license_plate,
            data.brand,
            data.model,
            data.color,
            data.type,
            data.owner_id
        ))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

    return VehicleResponse(
        vehicle_id=vehicle_id,
        license_plate=data.license_plate,
        brand=data.brand,
        model=data.model,
        color=data.color,
        type=data.type,
        owner_id=data.owner_id
    )


@router.get("/{license_plate}", response_model=VehicleResponse)
def get_vehicle_by_plate(license_plate: str):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT vehicle_id, license_plate, brand, model, color, type, owner_id, registered_at
            FROM vehicles
            WHERE license_plate = %s
        """, (license_plate,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Vehicle not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

    return VehicleResponse(
        vehicle_id=row[0],
        license_plate=row[1],
        brand=row[2],
        model=row[3],
        color=row[4],
        type=row[5],
        owner_id=row[6],
        registered_at=row[7]
    )

