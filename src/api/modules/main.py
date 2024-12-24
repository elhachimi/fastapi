from fastapi import APIRouter

from .posts import routers as posts
from .comments import routers as comments
from .users import routers as users

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
