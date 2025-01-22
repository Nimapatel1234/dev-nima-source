from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database URL from .env file
DATABASE_URL = os.getenv("DATABASE_URL")  # e.g., postgresql://postgres:nima%40space123@localhost/new_book_pro

DATABASE_URL = "postgresql://postgres:nima%40space123@localhost/new_book_pro"

# Create database engine
engine = create_engine(DATABASE_URL)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
