def check_authorization(funcao):
    def validar_usuario(*args):
        usuario = args[0] 
        # Aqui validar o usuário/token
        if usuario.login == "admin":
            return funcao(*args)
        else:
            print(f" Login inválido {usuario.login}")
    return validar_usuario

class Usuario():
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

@check_authorization
def lista_pedidos(self):
    print(f"Retornar a lista de pedidos solicitado pelo {self.login}")

usuario = Usuario("admin", "qwe@123")
lista_pedidos(usuario)