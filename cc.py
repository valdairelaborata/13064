class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
       return self.__saldo
