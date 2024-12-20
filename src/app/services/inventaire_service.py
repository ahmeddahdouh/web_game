from src.app.repositories.inventaire_repoitory import InventaireRepository


class InventaireService:

    def __init__(self):
        pass

    @classmethod
    def create(self, db, inventory):
        return InventaireRepository.create_inventory(db, inventory)

    @classmethod
    def get_inventory_by_compte(self, db, id_compte):
        return InventaireRepository.get_inventory_by_compte(db, id_compte)

    @classmethod
    def edit_inventory_by_compte(self, db, inventory):
        return InventaireRepository.edit_inventory_by_compte(db, inventory)

    @classmethod
    def delete_inventory(self, db, inventory):
        return InventaireRepository.delete_inventory(db, inventory)
