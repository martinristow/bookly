from fastapi import FastAPI, status, HTTPException, APIRouter
from .schemas import CreateBook

router = APIRouter(tags=["Books"])


@router.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: CreateBook):
    return book_data
