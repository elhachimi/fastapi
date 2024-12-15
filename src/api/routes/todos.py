from fastapi import Request, Depends

from sqlalchemy.orm import Session

from fastapi import APIRouter

from database.session import get_db
from models import Todo

router = APIRouter()


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {"todos": todos}
