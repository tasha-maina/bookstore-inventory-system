# db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("DATABASE_USER", "postgres")
PASSWORD = os.getenv("DATABASE_PASSWORD", "")
HOST = os.getenv("DATABASE_HOST", "localhost")
PORT = os.getenv("DATABASE_PORT", "5432")
DB_NAME = os.getenv("DATABASE_NAME", "bookstore_db")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = SessionLocal()

Base = declarative_base()
