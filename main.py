


from model.model import Cliente
from infra.infra import db




cliente = Cliente(nome="Ana", email="ana@gmail.com")
db.add(cliente)
db.commit()
