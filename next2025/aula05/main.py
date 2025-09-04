from sqlalchemy.orm import Session

from utils.db_utils import get_engine
from models.base import Base
from models.user import User
from dao.user import UserDAO

DB_URL = "postgresql+psycopg2://postgres:next@localhost:5432/next2025"
engine = get_engine(DB_URL)

Base.metadata.create_all(engine)

with Session(engine) as session:
    user_dao = UserDAO(session)
    new_user = User(username="abc2", password="xyz", email="abc2@cesar.org")
    # user_dao.add_user(new_user)
    users = user_dao.list_users()
    print(users)
