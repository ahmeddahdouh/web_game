from src.app.repositories.objet_repository import ObjetRepository


class ObjetService:
    def __init__(self):
        pass

    @classmethod
    def create_objet(self, db, objet):
        return ObjetRepository.create_object(db, objet)

    @classmethod
    def get_all_object(self, db):
        return ObjetRepository.get_all_objects(db)
