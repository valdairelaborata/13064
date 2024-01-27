
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.cliente import model_cliente
from model.pedido import model_pedido

DATABASE_URL = "sqlite:///pedidos.db"
engine = create_engine(DATABASE_URL)

model_cliente.metadata.create_all(bind=engine)
# model_pedido.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()