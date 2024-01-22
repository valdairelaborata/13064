import unittest


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




class TestePessoa(unittest.TestCase):

    def teste_apresentar(self):
        pessoa = Pessoa("Ana", 30)
        apresentacao = pessoa.apresentar()
        self.assertEqual(apresentacao, "Olá, meu nome é Ana, tenho 30 anos!")


    def teste_eh_maior_de_idade(self):
        pessoa = Pessoa("Ana", 19)
        self.assertTrue(pessoa.eh_maior_de_idade())


    def teste_Neh_maior_de_idade(self):
        pessoa = Pessoa("Ana", 17)
        self.assertTrue(pessoa.neh_maior_de_idade())

    def teste_calculo(self):
        with self.assertRaises(ZeroDivisionError):
            pessoa = Pessoa("Ana", 30)
            pessoa.calculo()



unittest.main()