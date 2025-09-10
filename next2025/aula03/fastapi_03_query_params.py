"""Objetivo:

Uso de parâmetros de consulta de um endpoint com FastAPI."""

from fastapi import FastAPI

app = FastAPI()

items = list(range(1, 11))


# GET http://localhost:8000?offset=4&limit=3
@app.get("/")
async def get_list_of_numbers(offset: int = 0, limit: int = 5):
    """Query params."""
    begin = offset
    end = begin + limit

    return {"items": items[begin:end]}
