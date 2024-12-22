from fastapi import APIRouter

from .posts import routers as posts

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
