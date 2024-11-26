from typing import Optional

from pydantic import BaseModel, Field


class ObjetBase(BaseModel):

    nom_objet: str | None = Field(..., max_length=50)
    id_category_objet: int
    description_objet: str = Field(..., max_length=100)
    image_objet: Optional[str] = Field(default=None, sa_column_kwargs={"nullable": True})
