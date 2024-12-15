from sqlalchemy import Boolean, Column, Integer, String, Unicode

from database.session import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(Unicode(200))
    completed = Column(Boolean)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)


class Comment(Base):
    __tablename__ = "commkents"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Unicode(200), nullable=False)
