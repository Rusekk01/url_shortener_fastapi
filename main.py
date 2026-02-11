from fastapi import FastAPI
from contextlib import asynccontextmanager
from service import ShortURl
from database import init_db
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/short_link")
def get_short_link(long_url: str):
    
    return ShortURl().url

@app.post("/{short_url}")
def redirect():
    return "wdwq"

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)