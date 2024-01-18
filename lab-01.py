# # 1- Crie um decorador que verifica se o usuário está autenticado antes de executar uma função.

def autenticacao(funcao):
    def validar_usuario(usuario):
        if usuario.login != "Ana":
            print(f"Usuário inválido {usuario}")
        else:    
            funcao(usuario)

    return validar_usuario

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def __str__(self):
        return f"{self.login} - {self.senha}"


@autenticacao
def listar(usuario):
    print(f"Função listar executada após a validação do usuário {usuario}")


@autenticacao
def buscar(usuario):
    print(f"Função buscar executada após a validação do usuário {usuario}")

@autenticacao
def salvar(usuario):
    print(f"Função salvar executada após a validação do usuário {usuario}")

usuarioPedro = Usuario("Pedro", "123")
usuarioAna = Usuario("Ana", "456")

listar(usuarioPedro)

listar(usuarioAna)
buscar(usuarioPedro)
buscar(usuarioAna)
salvar(usuarioPedro)
salvar(usuarioAna)