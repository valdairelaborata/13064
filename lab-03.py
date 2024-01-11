class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.historico()


    def depositar(self, valor):
        self.saldo += valor
        self.historico()

    def sacar(self, valor):    
        if self.saldo < valor:
            print(f"Valor insuficiente. O saldo no momento é de {self.saldo}")
        else:
            self.saldo -= valor
            self.historico()
    
    def historico(self):
        print(f"O saldo é de {self.saldo}")


conta = Conta("Ana", 50)
conta.depositar(10)
conta.sacar(10)
conta.sacar(100)
conta.historico()
conta.sacar(40)