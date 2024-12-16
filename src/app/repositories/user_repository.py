from sqlalchemy.exc import IntegrityError
from src.app.models.user_model import User
from src.app.schemas.user_schema import UserBase
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from src.config.sécurité.securité import (
    verify_password,
    create_access_token,
    hash_password,
)


class UserRepo:
    def __init__(self):
        pass

    def create_user(db, user: UserBase):
        user_db = User(
            user_login=user.user_login,
            user_login_date=user.user_login_date,
            hashed_password=hash_password(user.password),
            user_role=user.user_role,
            compte_id=user.compte_id,
        )
        try:
            db.add(user_db)
            db.commit()
            db.refresh(user_db)
            return user_db
        except IntegrityError as ei:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Violation de contrainte d'intégrité : {str(ei.orig) if ei.orig else str(ei)}",
            )
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Erreur lors de la création de l'utilisateur : {str(e)}",
            )

    @classmethod
    def read_users(self, db):
        return db.query(User).all()

    @classmethod
    def read_user_by_login(self, db, login):
        try:
            user_db = db.query(User).filter(User.user_login == login).first()
            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"L'utilisateur {login} n'existe pas",
                )
            else:
                return user_db
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    @classmethod
    def get_token(self, db, username, password):
        user_db = db.query(User).filter(User.user_login == username).first()
        if not user_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"L'utilisateur {username} n'existe pas",
            )
        elif not verify_password(password, user_db.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )
        else:
            token = create_access_token(data={"sub": username,"password": password})
            return {
                "access_token": token,
                "token_type": "Bearer",
                "id_compte": user_db.compte_id,
            }
