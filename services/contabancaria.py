
from model.model import ContaBancaria
from infra.infra import db


def adicionar(numero, saldo, cliente_id):
    conta = ContaBancaria(numero=numero, saldo=saldo, cliente_id = cliente_id)
    db.add(conta)
    
    db.commit()




# parametro = 654321
# conta = db.query(ContaBancaria).filter(ContaBancaria.numero == parametro).first()
# print(f"A conta número: {conta.numero} - cliente: {conta.cliente.nome}")

