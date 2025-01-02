from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///db.sqlite"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()
