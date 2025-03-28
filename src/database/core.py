import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()


DB_URL = os.getenv("POSTGRES_URL")
engine = create_async_engine(DB_URL, future=True, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session