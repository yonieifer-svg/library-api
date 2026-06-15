from fastapi import APIRouter, HTTPException
from database.book_db import book_repo
from database.member_db import member_repo 
from schema import CreateBook, UpdateBook


router = APIRouter()

@router.post("", status_code=201)
def create_book(data: CreateBook):
    return book_repo.create_book(data)

@router.get("")
def get_all_books():
    return book_repo.get_all_books()

@router.get("/{id}")
def get_book_by_id(id: int):
    return book_repo.get_book_by_id(id)

@router.patch("/{id}")
def update_book(id: int, data: UpdateBook):
    return book_repo.update_book(id, data)

@router.patch("/{id}/borrow/{member_id}")
def set_unavailable(id: int, member_id: int):
    member = member_repo.get_member_by_id(member_id)
    if not member["is_active"]:
        raise HTTPException(400, "not active member")
    if member["total_borrows"] == 3:
        raise HTTPException(400, "max 3 borrows")
    
    is_available = book_repo.get_book_by_id(id)["is_available"]
    if not is_available:
        raise HTTPException(404, "book not available")
    
    return book_repo.set_available(id, False, member_id)

@router.patch("/{id}/return/{member_id}")
def set_available(id: int, member_id: int):
    borrowed_by = book_repo.get_book_by_id(id)["borrowed_by"]
    if borrowed_by != member_id:
        raise HTTPException(400, "not the borrow")
    return book_repo.set_available(id, True, None)

