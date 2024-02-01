
from fastapi import FastAPI
from pydantic import BaseModel

from services.produto import criar as criarProduto
from services.produto import buscar as buscarProduto
from services.produto import alterar as alterarProduto
from services.produto import excluir as excluirProduto


app = FastAPI()


class ProdutoView(BaseModel):
    codigo: str
    descricao: str


#CRUD

#C - criar
@app.post("/produtos")
def criar(produtoView: ProdutoView):
    criarProduto(produtoView.codigo, produtoView.descricao)
    return {"mensagem": f"Produto {produtoView.codigo} - {produtoView.descricao} criado!"}


#R - Ler
@app.get("/produtos/{id}")
def buscar(id: int):
    return buscarProduto(id)


#U - Alterar
@app.put("/produtos/{id}")
def alterar(id:int, produtoView: ProdutoView):
    alterarProduto(id, produtoView.codigo, produtoView.descricao)
    return {"mensagem": f"Produto {produtoView.codigo} - {produtoView.descricao} alterado!"}


#D - Excluir
@app.delete("/produtos/{id}")
def delete(id: int):
    excluirProduto(id)
    return {"mensagem": f"Produto excluído. {id}"}



# from services.cliente import alterar, listar_contas
# from services.contabancaria import adicionar

# # adicionar("Claúdia", "claudia@gmail.com")

# alterar(3, "Ana Cláudia")

# # listar_contas(3)

# # adicionar(987, 8000, 3)