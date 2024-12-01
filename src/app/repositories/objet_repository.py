from src.app.models.objet_model import Objet


class ObjetRepository:
    def __init__(self):
        pass

    @classmethod
    def create_object(self, db, objet):
        db_objet = Objet(
            nom_objet=objet.nom_objet,
            id_category_objet=objet.id_category_objet,
            description_objet=objet.description_objet,
            image_objet=objet.image_objet,
        )

        db.add(db_objet)
        db.commit()
        db.refresh(db_objet)
        return db_objet

    @classmethod
    def get_all_objects(self, db):
        return db.query(Objet).all()

    @classmethod
    def get_object_by_id(self, db, id_objet):
        return db.query(Objet).filter_by(id_objet=id_objet).first()
