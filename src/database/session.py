from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from ..settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)

# Create the Database Tables
SQLModel.metadata.create_all(engine)

# Dependency to get DB Session


def get_session():
    with Session(engine) as session:
        yield session
