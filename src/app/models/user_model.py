from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class User(SQLModel, table=True):
    id_user:  Optional[int] = Field(default=None, primary_key=True)
    user_login: str = Field(..., max_length=50, sa_column_kwargs={"nullable": False})
    hashed_password: Optional[str] = Field(
        default=None, sa_column_kwargs={"nullable": False}
    )
    user_created_at: datetime = Field(default_factory=datetime.utcnow)
    user_login_date: datetime = Field(default_factory=datetime.utcnow)
    user_role: str = Field(..., max_length=20)
    compte_id: int = Field(foreign_key="compte.id_compte", nullable=False, unique=True)
    compte: Optional["Compte"] = Relationship(back_populates="user")
