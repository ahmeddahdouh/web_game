from typing import Annotated
from urllib.request import Request
from fastapi import APIRouter, Depends
from fastapi.openapi.models import OAuth2
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.app.schemas.user_schema import UserBase
from src.app.services.user_service import UserService
from src.config.db.database import db_dependency

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/")
async def create_user(db: db_dependency, user: UserBase):
    return UserService.create_user(db, user)


@user_router.get("/")
async def read_users(db: db_dependency):
    return UserService.read_users(db)


@user_router.get("/{login}")
async def read_user(db: db_dependency, login: str):
    return UserService.read_user_by_login(db, login)
