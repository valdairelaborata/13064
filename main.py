# 1 - Criar uma classe ContaBancaria em um módulo separado e usá-la em um script principal. Certifique-se de criar a estrutura de diretórios apropriada para o projeto.

from contabancaria.conta import ContaBancaria
conta = ContaBancaria(32132154, 10)

conta.depositar(50)
print(conta.comprovante())
