from fastapi import APIRouter, HTTPException
from uuid import uuid4
from datetime import datetime
from app.schemas.user import UserProfileCreate, UserProfileResponse
from app.database.db import get_connection

router = APIRouter()

@router.post("/create", response_model=UserProfileResponse)
def create_profile(profile: UserProfileCreate):
    profile_id = str(uuid4())
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO user_profiles (profile_id, user_id, full_name, phone_number, address)
            VALUES (%s, %s, %s, %s, %s)
        """, (profile_id, profile.user_id, profile.full_name, profile.phone_number, profile.address))
        conn.commit()

        return UserProfileResponse(
            profile_id=profile_id,
            user_id=profile.user_id,
            full_name=profile.full_name,
            phone_number=profile.phone_number,
            address=profile.address,
            created_at=datetime.utcnow()
        )
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating profile: {str(e)}")
    finally:
        cur.close()
        conn.close()

@router.get("/{user_id}", response_model=UserProfileResponse)
def get_profile(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT profile_id, user_id, full_name, phone_number, address, created_at
            FROM user_profiles
            WHERE user_id = %s
        """, (user_id,))
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Profile not found")
        return UserProfileResponse(
            profile_id=row[0],
            user_id=row[1],
            full_name=row[2],
            phone_number=row[3],
            address=row[4],
            created_at=row[5]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cur.close()
        conn.close()


