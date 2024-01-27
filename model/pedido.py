
from sqlalchemy import Column, Float, ForeignKey, Integer,  String
from sqlalchemy.orm import declarative_base, relationship

model_pedido = declarative_base()

class Pedido(model_pedido):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    valor = Column(Float)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="pedidos")

