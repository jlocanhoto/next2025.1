"""Objetivo:

Uso do corpo da resposta em um endpoint com FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4


class UserRequest(BaseModel):
    name: str
    age: int


class UserResponse(UserRequest):
    id: str


app = FastAPI()


@app.post("/users")
async def add_new_user(user: UserRequest) -> UserResponse:
    """Request body."""
    return UserResponse(id=str(uuid4()), **user.model_dump())
