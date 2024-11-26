from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Objet(SQLModel, table=True):
    id_objet: int | None = Field(default=None, primary_key=True)
    nom_objet: str | None = Field(..., max_length=50)
    id_category_objet: int = Field(foreign_key="category.id_category", nullable=False)
    description_objet: str = Field(..., max_length=100)
    image_objet: Optional[str] = Field(default=None, sa_column_kwargs={"nullable": True})

    category: Optional["Category"] = Relationship(back_populates="objets")
    inventaires : list["Inventaire"] = Relationship(back_populates="objets")

