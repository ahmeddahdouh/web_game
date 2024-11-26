from fastapi import APIRouter
from src.app.schemas.objet_schema import ObjetBase
from src.app.services.objet_service import ObjetService
from src.config.db.database import db_dependency

object_router = APIRouter( prefix="/object",tags=["Object"])


@object_router.post('/')
async def create_object(db:db_dependency,objet : ObjetBase):
    return ObjetService.create_objet(db,objet)

