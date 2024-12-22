from datetime import datetime
from typing import Optional, List

from ..posts.models import Post

from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: str = Field(sa_column_kwargs={"unique": True})
    posts: List["Post"] = Relationship(back_populates="user")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
