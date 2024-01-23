import unittest


# 1 - Crie uma classe ContaBancaria que permita depósitos, saques e verificação de saldo.
# Escreva testes para os métodos dessa classe.


class ContaBancaria:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def saldo(self):
       return self.__saldo

    def deposito(self, valor):
        self.__saldo += valor 

    def saque(self, valor):
        if self.__saldo < valor:
            print(f"Saldo insuficiente: {self.__saldo}")
        else:
            self.__saldo -= valor

    def saldo_adicional(self, valor):
        self.__saldo = 10/0


class TesteContaBancaria(unittest.TestCase):

    def teste_deposito(self):
        contaBancaria = ContaBancaria("0500680", 500)
        contaBancaria.deposito(500)
        self.assertEqual(contaBancaria.saldo, 1000)
        
    def teste_saque(self):
        contaBancaria = ContaBancaria("0500680", 500)
        contaBancaria.saque(500)
        self.assertEqual(contaBancaria.saldo, 0)

    def teste_saldo(self):
        contaBancaria = ContaBancaria("0500680", 500)
        self.assertFalse(contaBancaria.saldo < 0)
        
    def teste_saldo_adicional(self):
        with self.assertRaises(ZeroDivisionError):
            contaBancaria = ContaBancaria("0500680", 500)
            contaBancaria.saldo_adicional(500)


unittest.main()