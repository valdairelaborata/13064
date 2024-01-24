


from cadastro.pessoa import Pessoa


class Colaborador(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
