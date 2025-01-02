from src.database.session import get_session
from sqlmodel import Session, select
from fastapi import Depends
from src.api.modules.users.models import User, UserCreate
from src.core.security import get_password_hash, verify_password


def create_user(
    user_create: UserCreate, session: Session = Depends(get_session)
) -> User:
    db_obj = User.model_validate(
        user_create, update={"hashed_password": get_password_hash(user_create.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(
    email: str, session: Session = Depends(get_session)
) -> User | None:
    statement = select(User).where(User.email == email)
    session_user = session.exec(statement).first()

    return session_user


def authenticate_user(
    email: str, password: str, session: Session = Depends(get_session)
) -> User | None:
    db_user = get_user_by_email(session=session, email=email)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
