from fastapi import APIRouter
from .schemas import UserCreateModel

router = APIRouter(tags=["auth"])


@router.post("/signup")
async def create_user_account(user_data: UserCreateModel):
    pass