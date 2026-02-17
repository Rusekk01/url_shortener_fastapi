from repositories import Urls_repository
from crud import ShortURl


class URL_service():
    def __init__(self, session):
        self.repository = Urls_repository(session)
    
    async def gen_short_link(self, long_url: str):
        shorty = ShortURl().url
        await self.repository.add_new(long_url, shorty)
        return shorty
    
    async def get_by_short_link(self, shorty):
        res = await self.repository.get_by_short(shorty)
        return res