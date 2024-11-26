from src.app.models.category_model import Category


class CategoryRepository:
    def __init__(self):
        pass

    @classmethod
    def create_category(self, db ,category):
        category_db =  Category(
            nom_category=category.nom_category,
            description_category = category.description_category,
        )
        db.add(category_db)
        db.commit()
        db.refresh(category_db)
        return category_db