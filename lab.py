# 1- Crie uma classe chamada ContaBancaria que represente uma conta bancária básica. A conta deve ter um número de conta, um titular da conta e um saldo. Implemente os seguintes métodos mágicos:
# __init__(self, numero, titular, saldo): O construtor que inicializa os atributos da conta.
# __str__(self): O método que retorna uma representação em string da conta no formato "Conta de [titular]: [saldo]".
# Além dos métodos mágicos, implemente também os seguintes métodos:
# depositar(self, valor): Adiciona um valor ao saldo da conta.
# sacar(self, valor): Retira um valor do saldo da conta, desde que haja saldo suficiente..



class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__str__()

    @property
    def saldo(self):
       return self.__saldo

    def trocar_titular(self, titular, documento):
        self.__titular = titular
        print(f"Trocando o titular {documento}")

    def deposito(self, valor):
        self.__saldo += valor
        self.__str__()

    def sacar(self, valor):
        if self.__saldo < valor:
            print(f"Saldo insuficiente: {self.__saldo}")
        else:
            self.__saldo -= valor
            self.__str__()

    def __str__(self):
         print(f"Conta de {self.__titular}: {self.__saldo}")



conta = ContaBancaria("12345",  "João", 1000)
# print(conta)
conta.deposito(500)
# print(conta)
conta.sacar(200)
# print(conta)