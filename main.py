from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from service import ShortURl
from database import init_db, SessionDep
from schemas import UrlSchema
from models import Urls
from repositories import Urls_repository
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/short_link")
#async def get_short_link(long_url: UrlSchema, session: SessionDep):
#    shorty = ShortURl().url
#    session.add(Urls(
#        full_url = long_url.full_url,
#        short_url = shorty
#    ))
#    await session.commit()
#    return {"data": shorty }
#
async def get_short_link(long_url: UrlSchema, session: SessionDep):
    shorty = ShortURl().url
    await Urls_repository(session).add_new(long_url, shorty)
    return {"data": shorty }


@app.get("/{short_url}")
async def redirect(short_url: str, session: SessionDep):
    res = await Urls_repository(session).get_by_short(short_url)
    return RedirectResponse(url=res.full_url)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)