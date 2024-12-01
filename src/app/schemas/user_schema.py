from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    user_login: str = Field(..., max_length=50, sa_column_kwargs={"nullable": False})
    password: str
    user_created_at: datetime
    user_login_date: datetime
    user_role: str = Field(..., max_length=20)
    compte_id: int
