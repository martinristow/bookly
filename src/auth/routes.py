from fastapi import APIRouter, Depends
from .schemas import UserCreateModel
from .service import UserService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session

user = UserService()


router = APIRouter(tags=["auth"])


@router.post("/signup", response_model=UserCreateModel)
async def create_user_account(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)) -> dict:

    new_user = await user.create_user(user_data, session)

    return new_user