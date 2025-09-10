from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from views.login import login_router
from api import api_router

app = FastAPI()

app.include_router(login_router)
app.include_router(api_router)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
