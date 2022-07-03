from sqlalchemy import Column, Text, Integer, VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

from config.config import DB_URL, DB_POOL_SIZE, DB_CONNECTION_TIMEOUT_S


Base = declarative_base()
engine = create_async_engine(
    DB_URL, pool_size=DB_POOL_SIZE, pool_timeout=DB_CONNECTION_TIMEOUT_S
)


class Urls(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    short_id = Column(VARCHAR(255), nullable=False, unique=True)
    long_url = Column(Text, nullable=False, unique=True)

    def __repr__(self):
        return f"Urls(id={self.id}, short_id={self.short_id}, long_url={self.long_url})"


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
