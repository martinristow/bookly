from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import List
from src.books.schemas import Book
from src.reviews.schemas import ReviewModel
import uuid


class UserModel(BaseModel):
    username: str = Field(min_length=3, max_length=8)
    email: EmailStr = Field(max_length=40)
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    password_hash: str = Field(min_length=6)


class UserCreateModel(UserModel):
    pass


class UserResponseModel(UserModel):
    uid: uuid.UUID
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    update_at: datetime


class UserBooksModel(UserResponseModel):
    books: List[Book]
    reviews: List[ReviewModel]


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str