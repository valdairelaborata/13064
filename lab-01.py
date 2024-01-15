# 1- Considere uma classe de Conta Bancária e aplique os conceitos de encapsulamento para movimentar o saldo e a troca do titular.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        self.__comprovante()

    @property
    def saldo(self):
       return self.__saldo

    def trocar_titular(self, titular, documento):
        self.__titular = titular
        print(f"Trocando o titular {documento}")
        self.__comprovante()

    def deposito(self, valor):
        self.__saldo += valor
        self.__comprovante()

    def sacar(self, valor):
        self.__saldo -= valor
        self.__comprovante()

    def __comprovante(self):
        print(f"Conta do titular {self.__titular} com saldo de: {self.__saldo}")



conta = ContaBancaria("Ana", 500)
conta.deposito(10)
conta.sacar(20)
conta.deposito(10)
print(conta.saldo)

conta.trocar_titular("Pedro", "xpto 0010")
conta.sacar(20)
conta.deposito(10)
