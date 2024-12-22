from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Comment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    content: str
    published: bool = Field(default=False)
    updated_at: Optional[datetime] = Field(default=None)
