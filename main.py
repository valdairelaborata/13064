
# 1 - Crie um modelo de dados de Cliente. Com esse modelo de dados crie o banco e as operações CRUD
# Para o cliente é necessário armazenar o nome e e-mail.


from services.cliente import atualizar_cliente, excluir_cliente, incluir_cliente, ler_clientes

#C
incluir_cliente("Pedro", "pedro@gmail.com")

#R
clientes = ler_clientes()
for cliente in clientes:
    print(f"Id: {cliente.id} - nome: {cliente.nome} - e-mail: {cliente.email}")

#U
atualizar_cliente(1, "Pedro alterado", "pedroalterado@gmail.com")
    
#D
#excluir_cliente(1)    
    


