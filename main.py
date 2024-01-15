
class Veiculo(object):
    def __init__(self, modelo, placa) :
        self.modelo = modelo
        self.placa = placa

    # def __del__(self):
    #     print(f"Objeto {self.modelo} sendo destruído")
   
    def __str__(self):
        return f"Veículo {self.modelo} - placa {self.placa}"

    def __repr__(self) :
        return f"Veículo (modelo='{self.modelo}', placa='{self.placa}')"
        

   
veiculo = Veiculo("Celta", "AKH 0725")

# del veiculo

print(veiculo)
print(repr(veiculo))

print("Fim")