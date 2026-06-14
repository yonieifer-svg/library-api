from fastapi import FastAPI
from database.db_connection import db
from database.book_db import book_repo
from routes.book_routes import router as book_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["books"])




