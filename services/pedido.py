

from model.model import Pedido
from infra.infra import db


def incluir_pedido(descricao, valor, cliente_id):
    pedido = Pedido(descricao=descricao, valor=valor, cliente_id=cliente_id)
    db.add(pedido)
    db.commit()

def obter_cliente(id):
    pedido = db.query(Pedido).filter(Pedido.id == id).first()
    print(f"Cliente do pedido id: {pedido.id} é o: {pedido.cliente.nome}")