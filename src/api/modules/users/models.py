import uuid
from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..posts.models import Post

from sqlmodel import SQLModel, Field, Relationship


# Shared properties


class UserBase(SQLModel):
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    email: str = Field(sa_column_kwargs={"unique": True})
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Properties to receive on user creation


class UserCreate(UserBase):
    password: str


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    posts: List["Post"] = Relationship(back_populates="user")


# Properties returned via API


class UserPublic(UserBase):
    id: uuid.UUID


# JSON payload containing access token


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None
