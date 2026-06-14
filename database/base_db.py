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

        cursor = self.db.connection.cursor()
        cursor.execute(query, values)
        self.db.connection.commit()
        cursor.close()


    def find(self, filter=None):
        filter_query = ""
        values = ""

        if filter:
            filter_query = f" WHERE {" AND ".join([key + " = %s" for key in filter])}"
            values = list(filter.values())

        query = f"SELECT * FROM {self.table}" + filter_query

        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return result
    

    def update(self, id: int, data: dict):
        set_items = f"{", ".join([key + " = %s" for key in data])}"
        
        query = f"UPDATE {self.table} SET {set_items} WHERE id = %s"

        cursor = self.db.connection.cursor()
        cursor.execute(query, list(data.values()) + [id])
        self.db.connection.commit()
        cursor.close()


    def count(self, filter=None):
        filter_query = ""
        values = ""

        if filter:
            filter_query = f" WHERE {" AND ".join([key + " = %s" for key in filter])}"
            values = list(filter.values())

        query = f"SELECT COUNT(*) AS total FROM books" + filter_query

        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return result["total"]
    
