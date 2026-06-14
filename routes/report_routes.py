from fastapi import APIRouter
from database.member_db import member_repo
from database.book_db import book_repo


router = APIRouter()

@router.get("/summary")
def get_summary():
    return {
        "total books": book_repo.count_total_books(),
        "available books": book_repo.count_available_books(),
        "currently borrowed": book_repo.count_borrowed_books(),
        "active members": member_repo.count_active_members()
    }


@router.get("/books-by-genre")
def get_books_by_genre():
    query = f"SELECT genre AS genre, COUNT(*) as count FROM {book_repo.table} GROUP BY genre"
    with book_repo.db.get_connection() as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        

@router.get("/top-member")
def get_top_member():
    top = member_repo.get_top_member()
    return {"member_id": top["id"], "borrowed": top["total_borrows"]}

