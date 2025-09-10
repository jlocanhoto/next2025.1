"""Objetivo:

Uso de parâmetros de rota de um endpoint com FastAPI."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def get_user_info(user_id: int = 0):
    """Path params."""
    return {"userId": user_id}
