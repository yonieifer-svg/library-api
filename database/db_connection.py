import mysql.connector


class DB:
    def __init__(self):
        self.connect()
        self.init_db()
        self.init_tables()

    def connect(self):
        self._connection = mysql.connector.connect(host = "localhost",
                                   port = 3306,
                                   user = "root",
                                   password = "root")

    def init_db(self):
        cursor = self.connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS library")
        cursor.execute("USE library")
        cursor.close() 

    def init_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
            id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(50) NOT NULL,
            author VARCHAR(50) NOT NULL,
            genre ENUM("Fiction", "Non-Fiction", "Science", "History", "Other") NOT NULL,
            is_available BOOL NOT NULL,
            borrowed_by_member_id INT NULL
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
        cursor.close()

    @property
    def connection(self):
        if not self._connection or not self._connection.is_connected():
            self.connect()
        return self._connection

try:
    db = DB()
except Exception as e:
    print(e)
    raise 

