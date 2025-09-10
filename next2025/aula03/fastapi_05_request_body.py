"""Objetivo:

Uso do corpo da requisição em um endpoint com FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.post("/users")
async def add_new_user(user: User) -> User:
    """Request body."""
    user.name += " Lucas"
    user.age += 10
    return user
