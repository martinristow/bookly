from pydantic import BaseModel


class CreateBook(BaseModel):
    title: str
    author: str
