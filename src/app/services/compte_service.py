from pathlib import Path

from src.app.repositories.compte_repository import CompteRepository


class CompteService:
    def __init__(self):
        pass

    @classmethod
    def create_compte(self, compte, db):
        return CompteRepository.create_compte(compte, db)

    @classmethod
    def get_all_comptes(self, db):
        return CompteRepository.get_all_comptes(db)

    @classmethod
    def get_compte_by_id(self, db, compte_id):
        return CompteRepository.get_compte_id(db, compte_id)
