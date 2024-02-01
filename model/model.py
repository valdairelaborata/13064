

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    email = Column(String)

    contas = relationship("ContaBancaria", back_populates="cliente")


class ContaBancaria(Base):
    __tablename__ = "contasBancarias"
    id = Column(Integer, primary_key=True, index=True)
    numero =Column(Integer)
    saldo = Column(Float)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="contas")


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String)
    descricao = Column(String)