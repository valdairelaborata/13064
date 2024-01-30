from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.model import Base

DATABASE_URL = "sqlite:///gestaoContas.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()