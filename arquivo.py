
def gerador_arquivo(caminho):
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            yield linha


for linha in gerador_arquivo('dados.txt'):    
    print(linha.strip())