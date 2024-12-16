from src.app.models.category_model import Category


class CategoryRepository:
    def __init__(self):
        pass

    def create_category(db, category):
        category_db = Category(
            nom_category=category.nom_category,
            description_category=category.description_category,
        )
        db.add(category_db)
        db.commit()
        db.refresh(category_db)
        return category_db

    def get_all_categories(db):
        return db.query(Category).all()
