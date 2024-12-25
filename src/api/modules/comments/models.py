from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.api.modules.posts.models import Post


class Comment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    content: str
    post_id: int = Field(foreign_key="post.id")
    post: Optional["Post"] = Relationship(back_populates="comments")
    published: bool = Field(default=False)
    updated_at: Optional[datetime] = Field(default=None)
