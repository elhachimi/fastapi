from fastapi import APIRouter

from src.api.modules.posts import routers as posts
from src.api.modules.comments import routers as comments
from src.api.modules.users import routers as users

api_router = APIRouter()
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
