from src.api.modules.posts.models import Post
from src.api.modules.users.models import User
from src.api.modules.comments.models import Comment

from sqlmodel import SQLModel

__all__ = ["Post", "User", "Comment"]

metadata = SQLModel.metadata
