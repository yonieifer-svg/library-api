from database.base_db import BaseRepo
from database.db_connection import db


class MemberRepo(BaseRepo):
    def __init__(self, db, table):
        super().__init__(db, table)
    
    def create_member(self, data: dict):
        data["is_active"] = True
        data["total_borrows"] = 0
        return super().create(data)

    def get_all_members(self):
        return super().find()
    
    def get_member_by_id(self, id: int):
        return super().find({"id": id})
    
    def update_member(self, id: int, data: dict):
        return super().update(id, data)
    
    def deactive_member(self, id: int):
        return super().update(id, {"is_active": False})
    
    def active_member(self, id: int):
        return super().update(id, {"is_active": True})
    
    def increment_borrows(self, id: int):
        query = f"UPDATE {self.table} SET total_borrows = total_borrows + 1 WHERE id = %s"
        value = [id]

        with self.db.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, value)
                conn.commit()
    def count_active_members(self):
        return super().count({"is_active": True})
    
    def get_top_member(self):
        query = f"SELECT * FROM {self.table} ORDER BY total_borrows DESC LIMIT 1"

        with self.db.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                return result
            
member_repo = MemberRepo(db, "members")

    