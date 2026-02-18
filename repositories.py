from sqlalchemy import select
from models import Urls
from database import SessionDep
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

class Urls_repository():
    def __init__(self, session: SessionDep):
        self.local_session = session
    
    async def add_new(self, long_url, shorty):
        try:
            self.local_session.add(Urls(
            full_url = long_url,
            short_url = shorty
            ))
            await self.local_session.commit()
            return True
        except SQLAlchemyError as e:
            await self.local_session.rollback()
            return False
    
    async def get_by_short(self, short_url):
        query = select(Urls).filter(Urls.short_url == short_url)
        result = await self.local_session.execute(query)
        url_obj = result.scalars().first()
        if url_obj:
            return url_obj.full_url
        return None