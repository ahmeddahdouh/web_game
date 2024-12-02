from fastapi import HTTPException
from src.app.models.inventaire_model import Inventaire
from src.app.repositories.objet_repository import ObjetRepository
from sqlalchemy import and_


class InventaireRepository:
    def __init__(self):
        pass

    @classmethod
    def create_inventory(self, db, inventory):
        db_inventory = Inventaire(
            id_compte=inventory.id_compte,
            id_objet=inventory.id_objet,
            qty=inventory.qty,
        )
        try:
            db.add(db_inventory)
            db.commit()
            db.refresh(db_inventory)
            return db_inventory
        except Exception as e:
            db.rollback()
            if "UNIQUE constraint failed" in str(e.orig):
                raise HTTPException(status_code=409, detail="Violation de contrainte d'unicité.")
            elif "FOREIGN KEY constraint failed" in str(e.orig):
                raise HTTPException(status_code=400, detail="Violation de clé étrangère.")
            else:
                raise HTTPException(status_code=400, detail="Erreur d'intégrité.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erreur inconnue: {str(e)}")

    @classmethod
    def get_inventory_by_compte(self, db, id_compte):
        inventaires = db.query(Inventaire).filter(Inventaire.id_compte == id_compte).all()
        result = []

        for inventaire in inventaires:

            inventaire_dict = inventaire.__dict__
            objet = ObjetRepository.get_object_by_id(db, inventaire.id_objet)
            if objet:
                inventaire_dict["nom_objet"] = objet.nom_objet
            else:
                inventaire_dict["nom_objet"] = None

            result.append(inventaire_dict)

        return result

    @classmethod
    def edit_inventory_by_compte(self, db, inventory):
        element_bd = db.query(Inventaire).filter(
            and_(
                Inventaire.id_compte == inventory.id_compte,
                Inventaire.id_objet == inventory.id_objet
            )
        ).first()

        if element_bd:
            element_bd.qty = inventory.qty
            db.commit()
            db.refresh(element_bd)
            return element_bd
        else:
            raise HTTPException(status_code=404, detail="element Not found")

    @classmethod
    def delete_inventory(cls, db, inventory):
        element_bd = db.query(Inventaire).filter(
            and_(
                Inventaire.id_compte == inventory.id_compte,
                Inventaire.id_objet == inventory.id_objet
            )
        ).first()
        if element_bd:
            db.delete(element_bd)
            db.commit()
        else:
            raise HTTPException(status_code=404, detail="element Not found")

