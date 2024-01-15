# 1- Crie uma classe ContaBancaria que inclui funcionalidades básicas e uma classe ContaCorrente que herda da classe base. A classe derivada ContaCorrente substitui o método sacar para considerar um limite de saque além do saldo disponível. 


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



class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite): 
        self.__limite = limite     
        super().__init__(titular, saldo)

    def sacar(self, valor):
        if valor > self.saldo + self.__limite:
            print(f"Saldo + limite insuficiente {self.saldo + self.__limite}")
        else:
            return super().sacar(valor)    

# contaBancaria = ContaBancaria("Pedro", 200)


contaCorrente = ContaCorrente("Ana", 500, 1000)
contaCorrente.sacar(1000)
contaCorrente.sacar(100)
contaCorrente.deposito(5000)
contaCorrente.sacar(4500)
contaCorrente.sacar(1000)

contaCorrente2 = ContaCorrente("Pedro", 500, 2000)

contaCorrente2.sacar(1000)
contaCorrente2.sacar(100)
contaCorrente2.deposito(5000)
contaCorrente2.sacar(4500)
contaCorrente2.sacar(1000)