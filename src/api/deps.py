from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from src.database.session import get_session

# TODO add a api/v1 prefix to the routes using the settings.API_V1_STR variable
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/user/login/access-token")
SessionDep = Annotated[Session, Depends(get_session)]
TokenDep = Annotated[str, Depends(reusable_oauth2)]
