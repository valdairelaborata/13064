from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

model_cliente = declarative_base()

class Cliente(model_cliente):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    email = Column(String)

    pedidos = relationship("Pedido", back_populates="cliente")

class Pedido(model_cliente):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    valor = Column(Float)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="pedidos")
