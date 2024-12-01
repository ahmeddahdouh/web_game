from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel, Field


class CompteBase(BaseModel):
    nom: str = Field(..., max_length=50)
    prenom: str = Field(..., max_length=50)
    addresse: str = Field(..., max_length=100)
    score: int
    niveau: int
    avatar: str
