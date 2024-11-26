from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

from src.app.models.objet_model import Objet


class Category(SQLModel, table=True):
    id_category: int = Field(default=None, primary_key=True)
    nom_category: str
    description_category: Optional[str] = None

    # Liste d'objets liés à cette catégorie
    objets: List["Objet"] = Relationship(back_populates="category")


