
class Veiculo:
    def __init__(self, modelo, placa) :
        self.modelo = modelo
        self.placa = placa
        self.__velocidade = 0

    def descricao(self):
        return f"Modelo {self.modelo} - placa {self.placa} - velocidade {self.__velocidade}"



class Carro(Veiculo):
    def __init__(self, modelo, placa, capacidadeDoPortaMalas):
        self.capacidadeDoPortaMalas = capacidadeDoPortaMalas
        super().__init__(modelo, placa)
    
    def descricao(self):
        return super().descricao() + f" e tem {self.capacidadeDoPortaMalas} de porta malas"


class Moto(Veiculo):
    def __init__(self, modelo, placa, cilindrada):
        self.cilindrada = cilindrada
        super().__init__(modelo, placa)

    def descricao(self):
        return super().descricao() +  f" de {self.cilindrada}"
  


class Caminhao(Veiculo):
    def __init__(self, modelo, placa, carroceria):
        self.carroceria = carroceria
        super().__init__(modelo, placa)

    def descricao(self):
        return super().descricao() +  f" corroceria: {self.carroceria}"


carro = Carro("Celta", "AKH-0725", 250)
print(carro.descricao())

moto = Moto("Moto 01", "ASD-522", 125)
print(moto.descricao())
caminhao = Caminhao("Modelo 01", "SDF-2522", 8000)
print(caminhao.descricao())