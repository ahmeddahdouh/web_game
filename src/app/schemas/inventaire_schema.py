from pydantic import BaseModel, Field


class InventaireBase(BaseModel):
    id_compte: int
    id_objet: int
    qty: int
