from database.base_db import BaseRepo
from database.db_connection import db



class BookRepo(BaseRepo):
    def __init__(self, db, table):
        super().__init__(db, table)
    
    def create_book(self, data):
        data["is_available"] = True
        data["borrowed_by"] = None
        return super().create(data)
    
    def get_all_books(self):
        return super().find()
    
    def get_book_by_id(self, id: int):
        return super().find({"id": id})[0]
    
    def update_book(self, id, data):
        return super().update(id, data)
    
    def set_available(self, id:int , val:bool, member_id: int):
        return super().update(id, {"is_available": val, "borrowed_by": member_id})
    
    def count_total_books(self):
        return super().count()
    
    def count_available_books(self):
        return super().count({"is_available": True})
    
    def count_borrowed_books(self):
        return super().count({"is_available": False})
    
    def count_by_genre(self, genre):
        return super().count({"genre": genre})
    
    def count_active_borrows_by_member(self, member_id):
        return super().count({"borrowed_by": member_id})
    
    

book_repo = BookRepo(db, "books")


