
class Veiculo(object):
    def __init__(self, modelo, placa, valor) :
        self.modelo = modelo
        self.placa = placa
        self.valor = valor

    # def __del__(self):
    #     print(f"Objeto {self.modelo} sendo destruído")
   
    # def __str__(self):
    #     return f"Veículo {self.modelo} - placa {self.placa}"

    # def __repr__(self) :
    #     return f"Veículo (modelo='{self.modelo}', placa='{self.placa}')"

    def __add__(self, outro):
        return self.valor + outro.valor
    
    def __eq__(self, outro) :
        return self.modelo == outro.modelo
    
    def __ne__(self, outro):
        return not self.__eq__(outro)
    
    
   
veiculo1 = Veiculo("Celta", "AKH 0725", 12000)
veiculo2 = Veiculo("Fusca", "AKH 0725", 12000)

# print(veiculo1 + veiculo2)

# print(veiculo1 == veiculo2)

print(veiculo1 != veiculo2)

print("Fim")