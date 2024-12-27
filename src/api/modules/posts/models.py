import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from src.api.modules.users.models import User, UserPublic


# Shared properties


class PostBase(SQLModel):
    title: str
    description: Optional[str] = Field(default=None)
    published: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)


# Database model


class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    user: User = Relationship(back_populates="posts")


# Properties returned via API


class PostPublic(PostBase):
    user: UserPublic
