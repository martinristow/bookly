from fastapi import APIRouter, Depends
from src.db.models import User
from src.db.main import get_session
from .schemas import ReviewCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from .service import ReviewService
from src.auth.dependencies import get_current_user

review_service = ReviewService()

router = APIRouter(tags=["Reviews"])


@router.post("/book/{book_uid}")
async def add_review_to_books(book_uid: str, review_data: ReviewCreateModel,
                              current_user: User = Depends(get_current_user),
                              session: AsyncSession = Depends(get_session)):
    new_review = await review_service.add_review_to_book(user_email=current_user.email, review_data=review_data,
                                                   book_uid=book_uid, session=session)

    return new_review
