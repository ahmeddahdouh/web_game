from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Race(SQLModel,table = True):
    id_race: int | None = Field(default=None, primary_key=True)
    nom_race: str | None = Field(..., max_length=50)
    strength: int =Field( nullable=False,default=5)
    magic: str = Field(..., max_length=100)
    agility : int =Field( nullable=False,default=5)
    speed : int = Field( nullable=False,default=5)
    carisma : int = Field( nullable=False,default=5)
    chance : int = Field( nullable=False,default=5)

