from typing import Optional

from poetry.console.commands import self
from sqlmodel import Field, Relationship

from sqlmodel import SQLModel

from src.app.models.category_model import Category
from src.app.models.compte_model import Compte


class Inventaire(SQLModel , table = True):

    id_inventaire  : int = Field(primary_key = True)
    id_compte : int = Field(foreign_key = "compte.id_compte")
    id_objet : int = Field(foreign_key = "objet.id_objet")
    qunatity : int = Field(default= 0)

    compte: Optional["Compte"] = Relationship(back_populates="inventaires")
    category: Optional["Category"] = Relationship(back_populates="inventaires")