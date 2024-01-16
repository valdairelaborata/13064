
def meu_decorador(funcao):
    def wrapper():
        print(f"Antes da função")
        funcao()
        print(f"Depois da função")
    return wrapper


@meu_decorador
def minha_funcao():
    print(f"Minha funcão")


@meu_decorador
def outra_funcao():
    print(f"Outra função")


minha_funcao()
outra_funcao()