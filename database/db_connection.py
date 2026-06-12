import mysql.connector

def get_connection():
    conn = mysql.connector.connect(host = "localhost",
                                   port = 3306,
                                   user = "root",
                                   password = "root",
                                   database = "library_db")
    try:
        yield conn
    finally:
        conn.close()


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    sql_books_table = """
                    CREATE TABLE IF NOT EXISTS books (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(50) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    genre ENUM("Fiction", "Non-Fiction", "Science", "History", "Other") NOT NULL,
                    is_available BOOL NOT NULL,
                    borrowed_by_member_id INT NULL
                    )
                    """
    sql_members_table = """
                     CREATE TABLE IF NOT EXISTS members (
                     id INT PRIMARY KEY AUTO_INCREMENT,
                     name VARCHAR(50) NOT NULL,
                     email VARCHAR(50) UNIQUE NOT NULL,
                     is_active BOOL NOT NULL,
                     total_borrows INT NOT NULL
                     )
                    """
    cursor.execute(sql_books_table)
    cursor.execute(sql_members_table)
    cursor.close()
    conn.close()



