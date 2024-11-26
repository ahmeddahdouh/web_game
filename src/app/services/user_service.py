from src.app.repositories.user_repository import UserRepo


class UserService:
    def __init__(self):
        pass
    @classmethod
    def create_user(self,db,user):
        return UserRepo.create_user(db,user)

    @classmethod
    def read_users(self, db):
        return UserRepo.read_users(db)

    @classmethod
    def read_user_by_login(self, db, login):
        return UserRepo.read_user_by_login(db, login)

    @classmethod
    def get_token(self, db, username, password):
        return UserRepo.get_token(db, username, password)