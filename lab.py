# 1- Crie um gerador chamado gerador_pares que gere uma sequência infinita de números pares. Comece com o número 2 e gere os próximos números pares a partir dele. Em seguida, utilize um loop for para imprimir os primeiros 10 números pares gerados pelo seu gerador.



def gerador_pares(valor_maximo):
    for item in range(0, valor_maximo + 2, 2):
        yield item


gen = gerador_pares(20)
for numero in gen:
    print(numero)