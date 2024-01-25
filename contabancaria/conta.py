class ContaBancaria():
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def comprovante(self)    :
        return f"Conta nr: {self.numero} - saldo: {self.saldo}"