from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import settings

# Create async engine using create_async_engine
async_engine = create_async_engine(settings.DATABASE_URL, echo=True)


async def init_db():
    async with async_engine.begin() as conn:
        from src.books.models import Book
        # await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    # Use sessionmaker with correct type
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    # Ensure we yield the session in an async context
    async with Session() as session:
        yield session
