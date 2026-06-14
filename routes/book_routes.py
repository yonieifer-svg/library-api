from fastapi import APIRouter
from database.book_db import book_repo


router = APIRouter()

@router.post("", status_code=201)
def create_book(data: dict):
    return book_repo.create_book(data)

@router.get("")
def get_all_books():
    return book_repo.get_all_books()

@router.get("/{id}")
def get_book_by_id(id: int):
    return book_repo.get_book_by_id(id)

@router.patch("/{id}")
def update_book(id: int, data: dict):
    return book_repo.update_book(id, data)

@router.patch("/{id}/borrow/{member_id}")
def set_unavailable(id: int, member_id: int):
    return book_repo.set_available(id, False, member_id)

@router.patch("/{id}/return/{member_id}")
def set_available(id: int, member_id: int):
    return book_repo.set_available(id, True, None)

