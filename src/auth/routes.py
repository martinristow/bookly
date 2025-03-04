from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UserCreateModel, UserResponseModel
from .service import UserService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session

user_service = UserService()

router = APIRouter(tags=["auth"])


@router.post("/signup", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with email: {email} already exists")

    new_user = await user_service.create_user(user_data, session)

    return new_user
