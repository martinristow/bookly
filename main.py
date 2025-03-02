from fastapi import FastAPI
from src.books import routes
from contextlib import asynccontextmanager
from src.db.main import init_db


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

app.include_router(routes.router, prefix="/books")


#

@app.get("/")
async def home():
    return {"message": "hello world"}
