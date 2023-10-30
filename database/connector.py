from os import environ
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

# load .env file
load_dotenv()

#get database data from .env file
host = environ.get("DATABASE_HOST")
port = environ.get("DATABASE_PORT")
user = environ.get("DATABASE_USERNAME")
password = environ.get("DATABASE_PASSWORD")
db_name = environ.get("DATABASE_NAME")

# create database URL
DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"

# create sqlalchemy engine
engine = create_async_engine(DATABASE_URL, echo=True)

# create async session object
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """
    Function create and return Sqlalchemy session.
    :return: Sqlalchemy async session.
    """
    async with async_session() as session:
        # open and return session
        return session
