from fastapi import HTTPException

from sqlalchemy.orm import Session

from src.config.db.database import db_dependency
from src.app.models.compte_model import Compte
from src.app.schemas.compte_schema import CompteBase


class CompteRepository:

    def __init__(self):
        pass

    def create_compte(compte: CompteBase, db: Session):
        compte_db = Compte(
            nom=compte.nom,
            prenom=compte.prenom,
            addresse=compte.addresse,
            score=compte.score,
            niveau=compte.niveau,
            avatar=compte.avatar,
        )
        db.add(compte_db)
        db.commit()
        db.refresh(compte_db)
        return compte_db

    @classmethod
    def get_all_comptes(self, db: db_dependency):
        return db.query(Compte).all()

    @classmethod
    def get_compte_id(self, db, compte_id):
        db_compte = db.query(Compte).filter_by(id_compte=compte_id).first()
        if not db_compte:
            raise HTTPException(status_code=404, detail="Element not found")
        else:
            return db_compte
