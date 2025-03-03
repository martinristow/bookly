from pydantic import BaseModel, Field, EmailStr


class UserCreateModel(BaseModel):
    username: str = Field(min_length=3, max_length=8)
    email: EmailStr = Field(max_length=40)
    first_name: str
    last_name: str
    password_hash: str = Field(min_length=6, max_length=20)
