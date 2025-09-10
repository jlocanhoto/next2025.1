from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


def pagination_parameters(offset: int = 0, limit: int = 100):
    return {"offset": offset, "limit": limit}


class PaginationParameters:
    def __init__(self, offset: int = 0, limit: int = 100) -> None:
        self.offset = offset
        self.limit = limit


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(pagination_parameters)]):
    return commons


@app.get("/users/{user_id}/items")
async def read_items(
    user_id: str,
    commons: Annotated[PaginationParameters, Depends(PaginationParameters)],
):
    return {
        "user_id": user_id,
        "offset": commons.offset,
        "limit": commons.limit,
    }
