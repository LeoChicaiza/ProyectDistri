from pydantic import BaseModel
from typing import Optional

class ZoneCreate(BaseModel):
    level_id: str
    name: str

class ZoneResponse(BaseModel):
    zone_id: str
    level_id: str
    name: str

