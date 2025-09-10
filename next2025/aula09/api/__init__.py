from fastapi import APIRouter

from api.users import users_router
from api.auth import auth_router

api_router = APIRouter(prefix="/api")

api_router.include_router(users_router)
api_router.include_router(auth_router)
