"""Database configuration and session management module using Async SQLAlchemy."""

import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

load_dotenv()

DB_URL = os.getenv("DB_URL")

async_engine = create_async_engine(DB_URL, echo=False)

AsyncSessionFactory = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, autoflush=False, class_=AsyncSession
)


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Async context manager that provides an isolated AsyncSession.

    Yields:
        AsyncSession: An active SQLAlchemy async database session.
    """
    async with AsyncSessionFactory() as session:
        yield session
