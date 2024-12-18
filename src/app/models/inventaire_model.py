from typing import Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel
from src.app.models.compte_model import Compte


class Inventaire(SQLModel, table=True):  # Représente la table 'inventaire'
    id_compte: int = Field(
        foreign_key="compte.id_compte", primary_key=True
    )  # Référence à la table 'compte'
    id_objet: int = Field(
        foreign_key="objet.id_objet", primary_key=True
    )  # Référence à la table 'objet'
    qty: int = Field(default=0)

    # Relations
    compte: Optional["Compte"] = Relationship(
        back_populates="inventaires"
    )  # Relation avec Compte
    objet: Optional["Objet"] = Relationship(back_populates="inventaires")

    # Contrainte d'unicité sur la paire (id_compte, id_objet)
    __table_args__ = (
        UniqueConstraint("id_compte", "id_objet", name="uix_id_compte_objettt"),
    )
