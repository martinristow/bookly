from fastapi import status, HTTPException, APIRouter, Depends
from src.db.main import get_session
from .schemas import BookCreateModel, BookUpdateModel, Book
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService
from src.auth.dependencies import AccessTokenBearer

router = APIRouter(tags=["Books"])
book_service = BookService()
access_token_bearer = AccessTokenBearer()


@router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print(user_details)
    books = await book_service.get_all_books(session)
    return books


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session),
                        user_details=Depends(access_token_bearer)) -> dict:
    new_book = await book_service.create_book(book_data, session)

    return new_book


@router.get("/{book_uid}", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session),
                   user_details=Depends(access_token_bearer)) -> dict:
    book = await book_service.get_book(book_uid, session)

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    return book


@router.patch("/{book_uid}", response_model=Book)
async def update_book(book_uid: str, book_update_data: BookUpdateModel,
                      session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if not updated_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    return updated_book


@router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session),
                      user_details=Depends(access_token_bearer)):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if not book_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
