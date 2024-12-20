from fastapi import APIRouter

from api.routes import todos

api_router = APIRouter()
api_router.include_router(todos.router, prefix="/todos", tags=["todos"])
