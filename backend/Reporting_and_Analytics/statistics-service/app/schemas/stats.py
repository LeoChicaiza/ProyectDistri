
from pydantic import BaseModel

class StatsResponse(BaseModel):
    message: str
    total_visits: int
