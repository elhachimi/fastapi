from src.api.modules.posts.models import Post
from src.api.modules.users.models import User

from sqlmodel import SQLModel

__all__ = ["Post", "User"]

metadata = SQLModel.metadata
