
from comum.auxilar import FILESYSTEM
from pessoa import Pessoa

class Diretor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def apresentar(self):
        return super().apresentar() + " e sou o diretor."
    
    def salvar(self):
        print(f"Aqui vamos escrever no disco: {FILESYSTEM}")