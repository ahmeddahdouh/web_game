from src.app.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self):
        pass
    @classmethod
    def create_category(self,db,category):
        return CategoryRepository.create_category(db,category)