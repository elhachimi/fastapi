from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    title: str
    description: Optional[str] = Field(default=None)
    owner_id: int = Field(foreign_key="user.id")
    owner: "User" = Relationship(back_populates="posts")
    published: bool = Field(default=False)
    updated_at: Optional[datetime] = Field(default=None)
