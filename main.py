
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///pedidos.db"

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)


engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

def criar_cliente(nome):
    cliente = Cliente(nome=nome)
    db.add(cliente)
    db.commit()

def ler_clientes():
    return db.query(Cliente).all()


def atualizar_cliente(id, nome):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    cliente.nome = nome
    db.commit()

def excluir_cliente(id):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    db.delete(cliente)
    db.commit()

#C
#criar_cliente("Lucas")

#R
# clientes = ler_clientes()

# for cliente in clientes:
#     print(f"Id: {cliente.id} - nome: {cliente.nome}")

#U
#atualizar_cliente(1, "Ana alterado")
    
#D
#excluir_cliente(1)    
    


