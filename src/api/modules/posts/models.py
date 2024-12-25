from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from src.api.modules.comments.models import Comment
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.api.modules.users.models import User


class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    title: str
    description: Optional[str] = Field(default=None)
    owner_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="posts")
    comments: List["Comment"] = Relationship(back_populates="post")
    published: bool = Field(default=False)
    updated_at: Optional[datetime] = Field(default=None)
