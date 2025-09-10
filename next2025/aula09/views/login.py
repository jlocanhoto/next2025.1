from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

login_router = APIRouter()


@login_router.get("/login", response_class=HTMLResponse)
async def login_page():
    this_folder = Path(__file__).parent
    with open(this_folder.joinpath("login.html"), encoding="utf-8") as login_html_fp:
        return login_html_fp.read()
