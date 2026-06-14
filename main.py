from fastapi import FastAPI
from database.db_connection import db
from database.book_db import book_repo
from routes.book_routes import router as book_router
from routes.member_routes import router as member_router
from routes.report_routes import router as report_router

app = FastAPI()

app.include_router(book_router, prefix="/books", tags=["books"])

app.include_router(member_router, prefix="/members", tags=["members"])

app.include_router(report_router, prefix="/reports", tags=["reports"])




