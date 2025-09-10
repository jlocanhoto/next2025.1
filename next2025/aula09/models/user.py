from datetime import datetime

import sqlalchemy as sql
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(sql.String(255), unique=True)
    password: Mapped[str] = mapped_column(sql.String(255))
    email: Mapped[str] = mapped_column(sql.String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=sql.func.now()
    )
