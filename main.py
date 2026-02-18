from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from services import URL_service
from database import init_db, SessionDep
from schemas import UrlSchema
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/short_link")
async def get_short_link(data: UrlSchema, session: SessionDep):
    res = await URL_service(session).gen_short_link(data.full_url)
    return {"data": res }

@app.get("/{short_url}")
async def redirect(short_url: str, session: SessionDep):
    res = await URL_service(session).get_by_short_link(short_url)
    if res:
        return RedirectResponse(url=res)
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Короткая ссылка '{short_url}' не найдена"
        )

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)