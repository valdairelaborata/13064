

from model.cliente import Cliente
from infra.infra import db


def incluir_cliente(nome):
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
