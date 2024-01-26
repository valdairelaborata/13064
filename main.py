from services.cliente import atualizar_cliente, excluir_cliente, incluir_cliente, ler_clientes

#C
incluir_cliente("Pedro")

#R
clientes = ler_clientes()
for cliente in clientes:
    print(f"Id: {cliente.id} - nome: {cliente.nome}")

#U
atualizar_cliente(1, "Ana alterado")
    
#D
#excluir_cliente(1)    
    


