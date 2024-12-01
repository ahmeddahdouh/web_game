from pathlib import Path
from typing import Annotated, Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form
from starlette.staticfiles import StaticFiles
from src.app.schemas.compte_schema import CompteBase
from src.app.services.compte_service import CompteService
from src.config.db.database import db_dependency


compte_router = APIRouter(prefix="/compte", tags=["compte"])

UPLOAD_DIR = Path() / 'avatars'
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)



@compte_router.post('/')
async def create_compte(db: db_dependency,
                        nom: str = Form(..., max_length=50),
                        prenom: str = Form(..., max_length=50),
                        addresse: str = Form(..., max_length=100),
                        score: int = Form(...),
                        niveau: int = Form(...),
                        avatar: UploadFile = File(...)
                        ):
    data = await avatar.read()
    save_to = UPLOAD_DIR / avatar.filename
    avatar_url = f"/static/{avatar.filename}"
    account = CompteBase(
        nom=nom,
        prenom=prenom,
        addresse=addresse,
        score=score,
        niveau=niveau,
        avatar=avatar_url,
    )
    with open(save_to, 'wb') as f:
        f.write(data)
    return CompteService.create_compte(account,db)


@compte_router.get('/')
async def get_all_comptes(db: db_dependency):
    return CompteService.get_all_comptes(db)


@compte_router.get('/{compte_id}')
async def get_compte(db: db_dependency, compte_id: int):
    return CompteService.get_compte_by_id(db, compte_id)


# @compte_router.put('/{compte_id}')
# async def update_compte(db:db_dependency,compte_id:int,compte: CompteBase):
