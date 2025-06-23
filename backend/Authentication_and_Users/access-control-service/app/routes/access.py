from fastapi import APIRouter, HTTPException
from app.schemas.access import AccessControlCreate, AccessControlResponse
from app.database.db import get_connection
import uuid

router = APIRouter()

@router.post("/grant", response_model=AccessControlResponse)
def grant_access(data: AccessControlCreate):
    conn = get_connection()
    cur = conn.cursor()
    access_id = str(uuid.uuid4())
    try:
        cur.execute("""
            INSERT INTO access_controls (access_id, user_id, resource, permission_level)
            VALUES (%s, %s, %s, %s)
            RETURNING access_id, user_id, resource, permission_level, granted_at
        """, (access_id, data.user_id, data.resource, data.permission_level))
        result = cur.fetchone()
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return AccessControlResponse(
        access_id=result[0],
        user_id=result[1],
        resource=result[2],
        permission_level=result[3],
        granted_at=result[4]
    )

@router.get("/user/{user_id}", response_model=list[AccessControlResponse])
def get_user_permissions(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT access_id, user_id, resource, permission_level, granted_at
            FROM access_controls
            WHERE user_id = %s
        """, (user_id,))
        rows = cur.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return [
        AccessControlResponse(
            access_id=row[0],
            user_id=row[1],
            resource=row[2],
            permission_level=row[3],
            granted_at=row[4]
        ) for row in rows
    ]

