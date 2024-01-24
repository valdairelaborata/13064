from comum.auxilar import FILESYSTEM, obterConexaoComBancoDeDados
from comum.operacoes import raiz_quadrada
from comum.data import hora_agora
from cadastro.colaborador import Colaborador
from cadastro.diretor import Diretor

colaborador = Colaborador("Ana", 30)
print(colaborador.apresentar())

diretor = Diretor("Pedro", 55)
print(diretor.apresentar())
diretor.salvar()

# print(obterConexaoComBancoDeDados())

# print(FILESYSTEM)


# print(raiz_quadrada)

print(hora_agora)