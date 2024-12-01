from src.app.models.user_model import User
from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel


class Compte(SQLModel, table=True):  # Représente la table 'compte'
    id_compte: Optional[int] = Field(default=None, primary_key=True)
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    addresse: str = Field(..., max_length=100)
    score: int
    niveau: int
    avatar: Optional[str] = Field(default=None, sa_column_kwargs={"nullable": True})

    # Relations
    user: Optional["User"] = Relationship(
        back_populates="compte"
    )  # Relation avec User (si définie ailleurs)
    inventaires: List["Inventaire"] = Relationship(
        back_populates="compte"
    )  # Relation avec Inventaire
