from fastapi import FastAPI
from src.books import routes as book_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.auth import routes as auth_router


@asynccontextmanager
async def life_span(app: FastAPI):
    print("server is starting...")
    await init_db()
    yield
    print("server has been stopped!")


version = "v1"
app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router.router, prefix="/books")
app.include_router(auth_router.router, prefix="/auth")


#

@app.get("/")
async def home():
    return {"message": "hello world"}
