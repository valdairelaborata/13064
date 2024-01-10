class Carro(object):
    def __init__(self, cor, placa, status, tipo):
        self.cor = cor
        self.placa = placa
        self.status = status
        self.tipo = tipo
        self.temperatura = 30
        print("Opa, passei pelo construtor do carro.")


    def ligar(self):
        print(f"Ligando... o carro {self.placa}" )

    def acelerar(self):
        self.temperatura += 50

    def desligar(self):
        print(f"Desligando... o carro {self.placa}")

    def obterTemperaturaDoMotor(self):
        print(f"Opa, {self.temperatura} graus")
        



objetoCarro = Carro("Branca", "111111", "disponível", "hatch")
objetoCarro.ligar()
objetoCarro.acelerar()
objetoCarro.obterTemperaturaDoMotor()



print("Fim")
