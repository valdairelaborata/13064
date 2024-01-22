
# 2 - Crie um ambiente virtual chamado consulta_cep_env com venv no Python 3.12x e, em seguida, crie um script para consultar um CEP usando a API abaixo. 
# https://viacep.com.br/ws/{cep}/json/


import requests

response = requests.get("https://viacep.com.br/ws/81710230/json/")

if response.status_code == 200:
    dados = response.json()
    print(f"Logradouro: {dados["logradouro"]}")
    print(f"Bairro: {dados["bairro"]}")
    print(f"Cidade: {dados["localidade"]}")
    print(f"Estado: {dados["uf"]}")
else:
    print(f"Ocorreu um erro ao tentar consultar o cep. {response.status_code}")

