from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import AsyncGenerator
from app.common.base_model import BaseModel

async def main_db():
    engine = create_async_engine("sqlite+aiosqlite:///./bank_transactions.db", echo=True)
    metadata = MetaData()
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all) # Correct usage
    await engine.dispose()



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine("sqlite+aiosqlite:///./bank_transactions.db", echo=True)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)
    async with async_session() as session:
        yield session

async def init_db() -> None:
    engine = create_async_engine("sqlite+aiosqlite:///./bank_transactions.db", echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)