from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Capybara(BaseModel):
    id: str
    name: str
    weight: float
    health_status: str = "Healthy"
    last_seen: datetime = Field(default_factory=datetime.now)
    tags: List[str] = []

class Habitat(BaseModel):
    habitat_id: str
    location_coords: tuple[float, float]
    population_count: int
    environment_type: str  # e.g., "Swamp", "Riverbank"