import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/3")

if response.status_code == 200:
    data = response.json()
    print(f"Título: {data["title"]}")
    print(f"Dados: {data["body"]}")
else:
    print("Ocorreu um erro ao fazer a requisição.s")


