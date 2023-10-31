from fastapi import APIRouter
from src.apis.users import router as usersRouter

apis = APIRouter()
apis.include_router(usersRouter)

__all__ = ["apis"]
