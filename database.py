import os

from sqlmodel import SQLModel, Session, create_engine

try:
    # Load variables from .env when python-dotenv is installed.
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./rangmanch.db")

engine = create_engine(DATABASE_URL, echo=True)

def create_tables():
    """Create all tables defined in the SQLModel Class"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency that provides a database session for each request"""
    with Session(engine) as session:
        yield session