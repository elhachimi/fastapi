from database.session import get_session
from fastapi import APIRouter
from sqlmodel import Session
from fastapi import Depends
from .models import Comment


router = APIRouter()

# Create a new Comment


@router.post("/")
def create_comment(
    comment: Comment, session: Session = Depends(get_session)
) -> Comment:
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment
