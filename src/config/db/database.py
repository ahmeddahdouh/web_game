from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session
from src.config.db.config import DB_PASSWORD, DB_USER, DB_HOST, DB_NAME, DB_PORT


DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessoinLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = SessoinLocal()
    try:
        yield db
    finally:
        db.close()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


db_dependency = Annotated[Session, Depends(get_db)]
