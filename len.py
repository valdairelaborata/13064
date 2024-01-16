class ListaPersonalizada:
    def __init__(self, itens):
        self.__itens = itens
    
    def __len__(self):
        return len(self.__itens)

minha_lista = ListaPersonalizada([1, 2, 3, 4, 5, 6])
tamanho = len(minha_lista)
print(tamanho)  # Saída: 5
