from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from src.app.models.user_model import User

class Compte(SQLModel, table=True):  # Représente la table 'compte'
    id_compte: int | None = Field(default=None, primary_key=True)
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    addresse: str = Field(..., max_length=100)
    score: int
    niveau: int
    avatar: Optional[str] = Field(default=None, sa_column_kwargs={"nullable": True})

    # Relation correctement annotée avec User
    user: Optional["User"] = Relationship(back_populates="compte")
    inventaires: list["Inventaire"] = Relationship(back_populates="compte")
