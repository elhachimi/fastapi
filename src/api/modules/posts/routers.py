from typing import Sequence
from fastapi import Depends, HTTPException

from sqlmodel import Session, select

from fastapi import APIRouter

from database.session import get_session
from ..users.models import User
from .models import Post


router = APIRouter()

# Create a new post


@router.post("/")
def create_post(post: Post, session: Session = Depends(get_session)) -> Post:
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


# Read a post


@router.get("/{post_id}")
def read_post(post_id: int, session: Session = Depends(get_session)) -> Post:
    post = session.get(Post, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


# Update a post


@router.put("/{post_id}")
def update_post(
    post_id: int, updated_post: Post, session: Session = Depends(get_session)
) -> Post:
    post_db = session.get(Post, post_id)
    if not post_db:
        raise HTTPException(status_code=404, detail="Post not found")
    updated_post.id = post_id
    merged_post = session.merge(updated_post)
    session.commit()
    session.refresh(merged_post)
    return merged_post


# Delete a post


@router.delete("/{post_id}")
def delete_post(post_id: int, session: Session = Depends(get_session)) -> Post:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    session.delete(post)
    session.commit()
    return post


# Read a post


@router.get("/")
def list_posts(session: Session = Depends(get_session)) -> Sequence[Post]:
    statement = select(Post)
    results = session.exec(statement).all()
    return results
