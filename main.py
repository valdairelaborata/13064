
def aplicar(funcao, valor):
    return funcao(valor)

def dobrar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3


resultado1 = aplicar(dobrar, 5)
print(resultado1)
resultado2 = aplicar(triplicar, 5)
print(resultado2)

print("Fim")