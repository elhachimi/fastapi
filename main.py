from fastapi import FastAPI, Request, Depends, Form

from sqlalchemy.orm import Session


import models
from database import sessionLocal


app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return {"Hello": todos}


@app.post("/todos")
def save(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()

    return new_todo
