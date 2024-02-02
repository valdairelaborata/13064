
from datetime import datetime, timedelta
import jwt
from fastapi.security import OAuth2PasswordBearer

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

from services.produto import criar as criarProduto
from services.produto import buscar as buscarProduto
from services.produto import alterar as alterarProduto
from services.produto import excluir as excluirProduto


app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 10


class ProdutoView(BaseModel):
    codigo: str 
    descricao: str


def gerarToken(data: dict)  -> str:
    to_encode = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def validaToken(jwt: str):
    try:
        payload = jwt.decode(jwt, SECRET_KEY, algorithm=ALGORITHM)   
        return payload     
    except Exception:
        raise  HTTPException(status_code=401, detail="Acesso negado!")



@app.post("/token")
async def obterToken(usuario, senha):

    token_data = {"sub": usuario, "scopes": ["me"]}
    token = gerarToken(token_data)

    return {"access_token": token}



#CRUD

#C - criar
@app.post("/produtos")
def criar(produtoView: ProdutoView):
    criarProduto(produtoView.codigo, produtoView.descricao)
    return {"mensagem": f"Produto {produtoView.codigo} - {produtoView.descricao} criado!"}


#R - Ler
@app.get("/produtos/{id}")
def buscar(id: int, usuario: dict = Depends(validaToken)):
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
