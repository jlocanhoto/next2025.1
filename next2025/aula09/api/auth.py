from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Form
from pydantic import BaseModel
from dao.user import UserDAO
from dependencies.user_dao import get_user_dao
from utils import jwt_utils, password_utils

auth_router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    username: str
    password: str


# POST /api/login
@auth_router.post("/login")
async def login(
    user_dao: Annotated[UserDAO, Depends(get_user_dao)],
    login_form: LoginRequest = Form(...),
) -> Token:
    invalid_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!"
    )
    # ir no DB e verificar se o usuário existe através do username ou email
    user = user_dao.get_user_by_username_or_email(
        login_form.username, login_form.username
    )

    if user is None:
        raise invalid_credentials

    # comparar se a senha passada pelo login_form corresponde a senha salva no DB
    if not password_utils.validate_password(login_form.password, user.password):
        raise invalid_credentials

    # criar um token do tipo JWT para o usuário validado
    jwt_token = jwt_utils.create_jwt(user_id=str(user.id), expires_secs=3600)

    # retornar o token para o cliente
    return Token(access_token=jwt_token, token_type="Bearer")
