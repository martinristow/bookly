from pydantic import BaseModel
from datetime import datetime
import uuid


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_data: datetime
    page_count: int
    language: str
    created_at: datetime
    update_at: datetime


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_data: datetime
    page_count: int
    language: str


class BookUpdateModel(BookCreateModel):
    pass