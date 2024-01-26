

from model.cliente import Cliente
from infra.infra import db


def incluir_cliente(nome, email):
    cliente = Cliente(nome=nome, email=email)
    db.add(cliente)
    db.commit()

def ler_clientes():
    return db.query(Cliente).all()

def atualizar_cliente(id, nome, email):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    cliente.nome = nome
    cliente.email = email
    db.commit()

def excluir_cliente(id):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    db.delete(cliente)
    db.commit()
