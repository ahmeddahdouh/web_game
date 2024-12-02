from sys import prefix

from fastapi import APIRouter

from src.app.repositories.objet_repository import ObjetRepository
from src.app.schemas.inventaire_schema import InventaireBase
from src.app.services.inventaire_service import InventaireService
from src.config.db.database import db_dependency

inventaire_router = APIRouter(prefix="/inventaire", tags=["inventaire"])


@inventaire_router.post("/")
async def create_inventaire(db: db_dependency, inventory: InventaireBase):
    return InventaireService.create(db, inventory)


@inventaire_router.get("/")
async def get_inventory_by_compte(db: db_dependency, id_compte: int):

   return InventaireService.get_inventory_by_compte(db, id_compte)

@inventaire_router.put("/")
def edit_inventory_by_compte(db:db_dependency,inventory: InventaireBase):
    return InventaireService.edit_inventory_by_compte(db,inventory)

@inventaire_router.delete("/")
def delete_inventory_by_compte(db: db_dependency, inventory: InventaireBase):
    return InventaireService.delete_inventory(db,inventory)


