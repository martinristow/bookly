from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import settings


engine = AsyncEngine(create_engine(
    url=settings.DATABASE_URL,
    echo=True
))


async def init_db():
    async with engine.begin() as conn:
        # This code is for testing connection with database
        # statement = text("SELECT 'hello';")
        #
        # result = await conn.execute(statement)
        #
        # print(result.all())
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)

