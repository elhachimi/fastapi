from sqlalchemy import Boolean, Column, Integer, String, Unicode

from database import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(Unicode(200))
    completed = Column(Boolean)
