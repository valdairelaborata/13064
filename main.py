
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///pedidos.db"

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

def criar_cliente(nome):
    cliente = Cliente(nome=nome)
    db.add(cliente)
    db.commit()




criar_cliente("Ana")

print("Fim")

