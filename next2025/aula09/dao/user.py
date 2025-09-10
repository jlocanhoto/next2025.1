import sqlalchemy as sql
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from models.user import User


class UserDAO:
    def __init__(self, db_session: Session) -> None:
        self.session = db_session

    def get_user_by_username_or_email(self, username: str, email: str) -> User | None:
        return self.session.scalar(
            sql.select(User).where((User.username == username) | (User.email == email))
        )

    def user_exists(self, user: User) -> bool:
        existing_user = self.get_user_by_username_or_email(user.username, user.email)
        return existing_user is not None

    def add_user(self, user: User) -> None:
        if self.user_exists(user):
            raise ValueError("Usuário já cadastrado!")

        self.session.add(user)
        self.session.commit()

    def list_users(
        self, offset: int = 0, limit: int = 100, sort_by: str = "id", sort: str = "asc"
    ) -> list[User]:
        columns_mapping = {
            "id": User.id,
            "username": User.username,
            "email": User.email,
            "createdAt": User.created_at,
        }
        column = columns_mapping.get(sort_by, User.id)
        order_by = sql.desc(column) if sort == "desc" else sql.asc(column)
        statement = sql.select(User).order_by(order_by).limit(limit).offset(offset)
        users = self.session.scalars(statement).all()
        return list(users)

    def get_user(self, user_id: int) -> User | None:
        return self.session.scalar(sql.select(User).where(User.id == user_id))

    def update_user(self, user_id: int, new_user: User) -> User:
        try:
            update_user_sql = (
                sql.update(User)
                .where(User.id == user_id)
                .values(
                    username=new_user.username,
                    email=new_user.email,
                    password=new_user.password,
                )
                .returning(User)
            )

            result = self.session.execute(update_user_sql)
            self.session.commit()
        except IntegrityError as error:
            raise ValueError(
                f"Outro usuário já possui o username '{new_user.username}' ou email '{new_user.email}'"
            ) from error

        try:
            return result.scalar_one()
        except NoResultFound as error:
            raise KeyError(f"Usuário com id {user_id} não encontrado!") from error

    def delete_user(self, user_id: int) -> None:
        delete_user_sql = sql.delete(User).where(User.id == user_id)
        result = self.session.execute(delete_user_sql)

        if result.rowcount == 0:
            raise KeyError(f"Usuário com id {user_id} não encontrado!")

        self.session.commit()
