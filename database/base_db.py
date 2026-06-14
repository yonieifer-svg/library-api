from database.db_connection import DB


class BaseRepo:
    def __init__(self, db: DB, table):
        self.db = db
        self.table = table


    def create(self, data: dict):
        columns = ", ".join(data.keys())
        holders = ", ".join(["%s"] * len(data))
        values = list(data.values())

        query = f"INSERT INTO {self.table} ({columns}) VALUES ({holders})"

        with self.db.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, values)
                conn.commit()


    def find(self, filter=None):
        filter_query = ""
        values = ""

        if filter:
            filter_query = f" WHERE {" AND ".join([key + " = %s" for key in filter])}"
            values = list(filter.values())

        query = f"SELECT * FROM {self.table}" + filter_query

        with self.db.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, values)
                result = cursor.fetchall()
                return result
    

    def update(self, id: int, data: dict):
        set_items = f"{", ".join([key + " = %s" for key in data])}"
        values = list(data.values()) + [id]

        query = f"UPDATE {self.table} SET {set_items} WHERE id = %s"

        with self.db.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, values)
                conn.commit()
        



    def count(self, filter=None):
        filter_query = ""
        values = ""

        if filter:
            filter_query = f" WHERE {" AND ".join([key + " = %s" for key in filter])}"
            values = list(filter.values())

        query = f"SELECT COUNT(*) AS total FROM {self.table}" + filter_query

        with self.db.get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query, values)
                result = cursor.fetchone()
                return result["total"]
            
    
