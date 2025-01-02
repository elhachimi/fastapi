from datetime import timedelta
from src.database.session import get_session
from typing import Annotated
from fastapi import APIRouter
from sqlmodel import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.api.modules.users.models import User, UserCreate, UserPublic, Token
from src.api.modules.users import crud
from src.core import security
from src.settings import settings
from src.api.deps import SessionDep


router = APIRouter()


@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, session: Session = Depends(get_session)) -> User:
    """
    Create a new user
    """

    db_user = crud.get_user_by_email(user.email, session)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.create_user(user, session)
    return new_user


@router.post("/login")
def login_access_token(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.authenticate_user(
        session=session, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return Token(
        access_token=security.create_access_token(
            user.id, expires_delta=access_token_expires
        )
    )
