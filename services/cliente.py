
from model.model import Cliente
from infra.infra import db


def adicionar(nome, email):
    cliente = Cliente(nome=nome, email=email)
    db.add(cliente)
    db.commit()

def listar_contas(cliente_id):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    print(f"Cliente: {cliente.nome}")
    for conta in cliente.contas:
        print(f"Numero: {conta.numero} - saldo: {conta.saldo}")

        
