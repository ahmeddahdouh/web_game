from src.app.repositories.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    def create_category(db, category):
        return CategoryRepository.create_category(db, category)

    @staticmethod
    def get_all_categories(db):
        return CategoryRepository.get_all_categories(db)
