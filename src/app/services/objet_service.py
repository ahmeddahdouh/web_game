from src.app.repositories.objet_repository import ObjetRepository


class ObjetService:
    def __init__(self):
        pass

    @classmethod
    def create_objet(self,db,objet):
        return ObjetRepository.create_object(db,objet)