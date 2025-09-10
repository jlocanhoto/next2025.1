from fastapi import APIRouter

from . import crud

router = APIRouter(prefix="/v1")
router.include_router(crud.router)
