from typing import Optional

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    nom_category: str
    description_category: str
