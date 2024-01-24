

class Pessoa():
    def __init__(self, nome, idade) :
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos!"
    
    def eh_maior_de_idade(self):
        return self.idade >= 18

    def neh_maior_de_idade(self):
        return self.idade < 18
    
    def calculo(self):
        resultado = 10 / 0


    