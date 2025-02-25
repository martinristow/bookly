from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "hello world"}


# @app.get("/greet/{name}")
# async def greet_name(name: str) -> dict:
#     return {"message": f"Hello {name}!"}


# @app.get("/greet")
# async def greet(name: str) -> dict:
#     return {"message": name}


@app.get("/greet")
async def greet(name: Optional[str] = None, age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}
