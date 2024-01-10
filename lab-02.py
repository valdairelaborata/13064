# 2 - Crie uma classe Calculadora com métodos para adição, subtração, multiplicação e divisão. Crie uma instância da classe e realize algumas operações.

class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = 0

    def adicao(self):
       self.resultado = self.numero1 + self.numero2
       self.exibirResultado("adição")

    def subtracao(self):
        self.resultado =  self.numero1 - self.numero2
        self.exibirResultado("subtracao")

    def multiplicacao(self):
        self.resultado = self.numero1 * self.numero2
        self.exibirResultado("multiplicação")

    def divisao(self):
        self.resultado = self.numero1 / self.numero2
        self.exibirResultado("divisão")

    def exibirResultado(self, observacao):
        print(f"O resultado da {observacao} é: {self.resultado}")


calculadora = Calculadora(10, 5)
calculadora.adicao() #15

calculadora2 = Calculadora(calculadora.resultado, 5)
calculadora2.subtracao()

# calculadora.subtracao()
# calculadora.multiplicacao()
# calculadora.divisao()

