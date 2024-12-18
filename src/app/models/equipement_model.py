from typing import Optional, List

from sqlalchemy import Column, JSON
from sqlmodel import Field, SQLModel, Relationship


class Equipment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: str
    weight: int
    slot: str
    allowed_classes: List[str] = Field(
        sa_column=Column(JSON)  # Stockage JSON dans la base de données
    )
    strength: int = Field(default=5)
    agility: int = Field(default=5)
    speed: int = Field(default=5)
    chance: int = Field(default=5)

