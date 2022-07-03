from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import delete, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from db.schema import engine, Urls


class Queries():
    def __init__(self):
        self.session = sessionmaker(bind=engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def get_next_id(self):
        async with self.session() as session:
            result = await session.execute(
                select(Sequence('urls_id_seq').next_value())
            )

            return result.scalar_one_or_none()

    async def get_long_url(self, short_id):
        async with self.session() as session:
            result = await session.execute(
                select(Urls.long_url).
                where(Urls.short_id == short_id)
            )

            return result.scalar_one_or_none()

    async def get_short_id(self, long_url):
        async with self.session() as session:
            result = await session.execute(
                select(Urls.short_id).
                where(Urls.long_url == long_url)
            )

            return result.scalar_one_or_none()

    async def add_url(self, short_id, long_url):
        async with self.session.begin() as session:
            ins = insert(Urls).values(short_id=short_id, long_url=long_url)

            await session.execute(ins)

    async def remove_url(self, short_id):
        async with self.session.begin() as session:
            result = await session.execute(
                delete(Urls).
                where(Urls.short_id == short_id)
            )

            return bool(result.rowcount)
