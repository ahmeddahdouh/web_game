from typing import Annotated

from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from src.app.endpoints.inventaire_endpoint import inventaire_router
from src.app.endpoints.objet_endpoint import object_router
from src.app.services.user_service import UserService
from src.config.db.database import create_db_and_tables, db_dependency
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.app.endpoints.compte_endpoints import compte_router, UPLOAD_DIR
from src.app.endpoints.user_endpoint import user_router
from src.app.endpoints.category_endpoint import category_router

app = FastAPI()
app.include_router(compte_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(object_router)
app.include_router(inventaire_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="avatars"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/token")
async def get_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    return UserService.get_token(db, form_data.username, form_data.password)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    create_db_and_tables()
    print("table created seccessfully")
