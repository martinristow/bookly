from fastapi import status, HTTPException, APIRouter, Depends
from src.db.main import get_session
from .schemas import BookCreateModel, BookUpdateModel, Book, BookDetailModel
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import BookService
from src.auth.dependencies import AccessTokenBearer
from src.auth.dependencies import RoleChecker
from src.errors import (BookNotFound)

router = APIRouter(tags=["Books"])
book_service = BookService()
access_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(['admin', 'user']))


@router.get("/", response_model=List[Book], dependencies=[role_checker])
async def get_all_books(session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    print(user_details)
    books = await book_service.get_all_books(session)
    return books


@router.get("/user/{user_uid}", response_model=List[Book], dependencies=[role_checker])
async def get_user_book_submissions(user_uid: str, session: AsyncSession = Depends(get_session),
                                    user_details=Depends(access_token_bearer)):
    print(user_details)
    books = await book_service.get_user_books(user_uid, session)
    return books


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book, dependencies=[role_checker])
async def create_a_book(book_data: BookCreateModel, session: AsyncSession = Depends(get_session),
                        token_details: dict = Depends(access_token_bearer)) -> dict:
    user_uid = token_details.get("user")["user_uid"]
    new_book = await book_service.create_book(book_data, user_uid, session)

    return new_book


@router.get("/{book_uid}", response_model=BookDetailModel, dependencies=[role_checker])
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session),
                   token_details: dict = Depends(access_token_bearer)) -> dict:
    book = await book_service.get_book(book_uid, session)

    if not book:
        raise BookNotFound()

    return book


@router.patch("/{book_uid}", response_model=Book, dependencies=[role_checker])
async def update_book(book_uid: str, book_update_data: BookUpdateModel,
                      session: AsyncSession = Depends(get_session),
                      token_details: dict = Depends(access_token_bearer)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if not updated_book:
        raise BookNotFound()

    return updated_book


@router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[role_checker])
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session),
                      token_details: dict = Depends(access_token_bearer)):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if not book_to_delete:
        raise BookNotFound()
