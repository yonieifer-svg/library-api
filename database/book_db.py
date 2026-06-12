import mysql.connector


class BookDB:
    def __init__(self, conn: mysql.connector.MySQLConnection):
        self.conn = conn
    

    def create_book(self, data: dict):
        try:
            with self.conn.cursor() as cursor:

                cursor.execute("""
                    INSERT INTO books 
                    (title, author, genre, is_available, borrowed_by_member_id)
                    VALUES (%s, %s, %s, True, NULL)
                """, [data["title"], data["author"], data["genre"]])

                self.conn.commit()
                return cursor.lastrowid
        except mysql.connector.Error:
            return None


    def get_all_books(self):
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM books")
            results = cursor.fetchall()
            return results


    def get_book_by_id(self, id: int):
         with self.conn.cursor(dictionary=True) as cursor:

            cursor.execute("""
                SELECT * FROM books
                WHERE id = %s
            """, [id])

            result = cursor.fetchone()
            return result


    def update_book(self, id: int, data: dict):
        if not data:
            return None
        
        with self.conn.cursor() as cursor:
            keys = ", ".join(f"{k} = %s" for k in data.keys())
            values = [v for v in data.values()] + [id]

            cursor.execute(f"""
                UPDATE books
                SET {keys}
                WHERE id = %s
            """, values)
            
            self.conn.commit()
            return cursor.rowcount > 0
         

    def set_available(self, id:int , val:bool, member_id: int):
        with self.conn.cursor() as cursor:

            cursor.execute("""
                UPDATE books
                SET is_available = %s, borrowed_by_member_id = %s
                WHERE id = %s
            """, [val, member_id, id])

            self.conn.commit()
            return cursor.rowcount > 0


    def count_total_books(self):
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT COUNT(*)  AS total FROM books")
            result = cursor.fetchone()
            return result["total"]

    def count_available_books(self):
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("""
                SELECT COUNT(*) AS total FROM books 
                WHERE is_available = True
            """)
            result = cursor.fetchone()
            return result["total"]

    def count_borrowed_books(self):
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("""
                SELECT COUNT(*) AS total FROM books 
                WHERE is_available = False
            """)
            result = cursor.fetchone()
            return result["total"]

    def count_by_genre(self, genre):
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("""
                SELECT COUNT(*) AS total FROM books 
                WHERE genre = %s
            """, [genre])
            result = cursor.fetchone()
            return result["total"]


    def count_active_borrows_by_member(self, member_id):
        with self.conn.cursor(dictionary=True) as cursor:
            cursor.execute("""
                SELECT COUNT(*) AS total FROM books 
                WHERE borrowed_by_member_id = %s
            """, [member_id])
            result = cursor.fetchone()
            return result["total"]