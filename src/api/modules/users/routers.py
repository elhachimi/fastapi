from src.database.session import get_session
from fastapi import APIRouter
from sqlmodel import Session
from fastapi import Depends
from src.api.modules.users.models import User


router = APIRouter()

# Create a new user


@router.post("/")
def create_user(user: User, session: Session = Depends(get_session)) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
