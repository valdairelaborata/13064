
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.cliente import Base

DATABASE_URL = "sqlite:///pedidos.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()