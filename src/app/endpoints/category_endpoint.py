from fastapi import APIRouter
from src.app.schemas.category_schema import CategoryBase
from src.app.services.category_service import CategoryService
from src.config.db.database import db_dependency

category_router = APIRouter(prefix="/category", tags=["category"])


@category_router.post("/")
async def create_new_category(db: db_dependency, category: CategoryBase):
    return CategoryService.create_category(db, category)


@category_router.get("/")
async def get_all_categories(db: db_dependency):
    return CategoryService.get_all_categories(db)
