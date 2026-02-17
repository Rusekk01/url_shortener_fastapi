from sqlalchemy import select
from models import Urls
from database import SessionDep
from schemas import UrlSchema

class Urls_repository():
    def __init__(self, session: SessionDep):
        self.local_session = session
    
    async def add_new(self, long_url, shorty):
        self.local_session.add(Urls(
        full_url = long_url,
        short_url = shorty
        ))
        await self.local_session.commit()
    
    async def get_by_short(self, short_url):
        query = select(Urls).filter(Urls.short_url == short_url)
        result = await self.local_session.execute(query)
        return result.scalars().first().full_url