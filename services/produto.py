

from model.model import Produto
from infra.infra import db

def criar(codigo, descricao):
    produto = Produto(codigo=codigo, descricao=descricao)
    db.add(produto)
    db.commit()

def buscar(id):
    produto = db.query(Produto).filter(Produto.id == id).first()
    return produto
    
def alterar(id, codigo, descricao):
    produto = db.query(Produto).filter(Produto.id == id).first()
    produto.codigo = codigo
    produto.descricao = descricao
    db.commit()

def excluir(id):
    produto = db.query(Produto).filter(Produto.id == id).first()
    db.delete(produto)
    db.commit()

