from pydantic import BaseModel, Field
from typing import Literal, Optional

class PlantBaseSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    scientific_name: str = Field(..., min_length=1, max_length=100)
    biome: str = Field(..., min_length=1, max_length=100)
    type: Literal["flower", "tree"]

class PlantCreateSchema(PlantBaseSchema):
    id: int = Field(..., gt=0)
    created_at: Optional[str] = None

class PlantResponseSchema(PlantBaseSchema):
    id: int
    created_at: str

    class Config:
        from_attributes = True
