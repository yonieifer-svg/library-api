import mysql.connector


class DB:
    def __init__(self):
        self.init_db()
        self.init_tables()

    def get_connection(self):
        return mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "root",
            database = "library")

    def init_db(self):
        conn  = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "root"
            )
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS library")
            cursor.execute("USE library")
        conn.close()

    def init_tables(self):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(50) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other') NOT NULL,
                    is_available BOOL NOT NULL,
                    borrowed_by INT NULL
                    )
                """)

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS members (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    is_active BOOL NOT NULL,
                    total_borrows INT NOT NULL
                    )
                """)

    

db = DB()



