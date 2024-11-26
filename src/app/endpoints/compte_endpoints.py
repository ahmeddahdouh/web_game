from typing import Annotated
from fastapi import APIRouter, Depends
from src.app.schemas.compte_schema import CompteBase
from src.app.services.compte_service import CompteService
from src.config.db.database import db_dependency
from src.config.sécurité.securité import oauth2_scheme

compte_router = APIRouter(prefix="/compte", tags=["compte"])

@compte_router.post('/')
async def create_create(compte_in : CompteBase,db:db_dependency):
    return CompteService.create_compte(db,compte_in)

@compte_router.get('/')
async def get_all_comptes(db:db_dependency):
    return CompteService.get_all_comptes(db)

@compte_router.get('/{compte_id}')
async def get_compte(db:db_dependency,compte_id:int,token: Annotated[str, Depends(oauth2_scheme)]):
            return CompteService.get_compte_by_id(db,compte_id)


#
# @compte_router.put('/{compte_id}')
# async def update_compte(db:db_dependency,compte_id:int,compte: CompteBase):