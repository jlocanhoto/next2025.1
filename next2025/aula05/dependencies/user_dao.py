from typing import Generator

from sqlalchemy.orm import Session

from utils.db_utils import get_engine
from models.base import Base
from dao.user import UserDAO


def get_user_dao() -> Generator[UserDAO, None, None]:
    DB_URL = "postgresql+psycopg2://postgres:next@localhost:5432/next2025"
    engine = get_engine(DB_URL)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        user_dao = UserDAO(session)
        yield user_dao
