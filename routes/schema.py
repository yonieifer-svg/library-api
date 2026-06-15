from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Optional

class CreateBook(BaseModel):
    title: str = Field(max_length=50)
    author: str = Field(max_length=50)
    genre: Literal['Fiction', 'Non-Fiction', 'Science', 'History', 'Other']

class UpdateBook(BaseModel):
    title: Optional[str] = Field(default=None, max_length=50)
    author: Optional[str] = Field(default=None, max_length=50)
    genre: Optional[Literal['Fiction', 'Non-Fiction', 'Science', 'History', 'Other']] = Field(default=None)

class CreateMember(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr

class UpdateMember(BaseModel):
    name: Optional[str] = Field(default=None, max_length=50)
    email: Optional[EmailStr] = Field(default=None)




