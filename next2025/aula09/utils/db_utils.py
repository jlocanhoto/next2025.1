import os

import sqlalchemy
from sqlalchemy_utils import create_database, database_exists


def _get_engine_url() -> str:
    DEFAULT_ENGINE_URL = "postgresql+psycopg2://postgres:next@localhost:5432/next2025"
    env_var_url = os.environ.get("DB_URL", DEFAULT_ENGINE_URL)
    return env_var_url


def get_engine(url: str | None = None) -> sqlalchemy.Engine:
    engine_url = url if url is not None else _get_engine_url()
    engine = sqlalchemy.create_engine(engine_url)

    if not database_exists(engine.url):
        create_database(engine.url)

    return engine
