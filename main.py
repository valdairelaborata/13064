class Carro:
    def __init__(self, cor, placa, status, tipo):
        self.cor = cor
        self.placa = placa
        self.status = status
        self.tipo = tipo
        print("Opa, passei pelo construtor do carro.")


    def ligar(self):
        print(f"Ligando... o carro {self.placa}" )

    def desligar(self):
        print(f"Desligando... o carro {self.placa}")



objetoCarro = Carro("Branca", "111111", "disponível", "hatch")
objetoCarro.ligar()


objetoCarro2 = Carro("Branca", "22222", "disponível", "hatch")
objetoCarro2.ligar()

print("Fim")
