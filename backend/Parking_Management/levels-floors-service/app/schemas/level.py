from pydantic import BaseModel

class LevelCreate(BaseModel):
    parking_lot: str
    level_number: int
    name: str  

class LevelResponse(BaseModel):
    level_id: str
    parking_lot: str
    level_number: int
    name: str

