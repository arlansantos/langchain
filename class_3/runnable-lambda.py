from langchain_core.runnables import RunnableLambda

""" Exemplo 1 - RunnableLambda"""

# Criando uma função customizada (adição de +1 à entrada)

def add_one(x: int) -> int:
    return x + 1

# transformando a minha função genérica em um Runnable do LagnChain, ou seja, ele implementa automáticamente os métodos
# `invoke` etc.

runnable = RunnableLambda(add_one)

# Executando...
resposta = runnable.invoke(1)

print("------ RESPOSTA DO INVOKE EXEMPLO 1 - RunnableLambda ------")
print(resposta)
print("-----------------------------------------------------------")
