This is an API server that connects to a database 
and manages a system of books and library members. 

=======================================================

Create docker with MyQql:
$ docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8

=======================================================

Folder structure:
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

=======================================================

Tables structure:
-books-
id
title
author
genre
is_available
borrowed_by

-members-
id
name
email
is_active
total_borrows

=======================================================

System rules:
-create book-
The user sends title, author, genre.

-create member-
The user sends name and email.

-genre-
Must be  Fiction / Non-Fiction / Science / History / Other.

-email-
Unique.

-non active member-
Can't borrow a book.

-unavailable book-
Cannot be borrowed.

-maximum books-
Member cannot hold more than 3 books at a time.

-Returning a book-
A book can only be returned if it is lent to the same member who is returning it.

=======================================================

Endpoints list:
-Books-
POST /books - create book
GET /books - all The books
GET /books/{id} - book by id
PATCH /books/{id} - update book
PATCH /books/{id}/borrow/{member_id} - borrow book to a member
PATCH /books/{id}/return/{member_id} - return book from a member.

-Members-
POST /members - create member
GET /members - all members
GET /members/{id} - member by id
PATCH /members/{id} - update member
PATCH /members/{id}/deactivate - deactivate member
PATCH /members/{id}/activate - activate member

-Reports-
GET /reports/summary - general report
GET /reports/books-by-genre - books by genre
GET /reports/top-member - the most active member

=======================================================

System flow:
request -> router -> database -> table

=======================================================

Running instructions:
uvicorn main:app


