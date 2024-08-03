from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import declarative_base
from os import getenv
from dotenv import load_dotenv
load_dotenv()

engine = create_async_engine(
    url=getenv('DATABASE_URL'),
    echo=True
)
session_factory = async_sessionmaker(bind=engine,expire_on_commit=False,autoflush=False,autocommit=False)
Base = declarative_base()