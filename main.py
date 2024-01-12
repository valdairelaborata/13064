
class Veiculo:
    def __init__(self, modelo, placa) :
        self.modelo = modelo
        self.placa = placa
        self.__velocidade = 0
        self.__tanque = 50

    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def tanque(self):
        return self.__tanque
    
    # @velocidade.setter
    # def velocidade(self, valor):
    #     self.__velocidade = valor
    

    def descricao(self):
        return f"Modelo {self.modelo} - placa {self.placa} - velocidade {self.__velocidade}"
     
    def acelerar(self):
        self.__consumir_combustivel(10)
        self.__velocidade += 10
  
    def freiar(self):
        self.__velocidade -= 5

    def __consumir_combustivel(self, litros):
        self.__tanque -= litros



   


class Carro(Veiculo):
    def __init__(self, modelo, placa, capacidadeDoPortaMalas):
        self.capacidadeDoPortaMalas = capacidadeDoPortaMalas
        super().__init__(modelo, placa)
    

    def descricao(self):
        return super().descricao() + f" e tem {self.capacidadeDoPortaMalas} de porta malas"
    
    def freiar(self):
        print(f"Freiando o carro")
        return super().freiar()


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
carro.acelerar()
carro.acelerar()
# carro.velocidade = 20
print(carro.descricao())
carro.tanque = 10


# carro.freiar()
# print(carro.descricao())
# print(carro.velocidade)




# moto = Moto("Moto 01", "ASD-522", 125)
# moto.acelerar()
# print(moto.descricao())
# moto.freiar()
# moto.freiar()
# print(moto.descricao())
    

# caminhao = Caminhao("Modelo 01", "SDF-2522", 8000)
# print(caminhao.descricao())