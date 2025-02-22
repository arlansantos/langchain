from langchain_core.runnables import RunnableLambda

""" Exemplo 2 - RunnableSequence """

def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

runnable_1 = RunnableLambda(add_one) # Convertendo a função de soma para runnable
runnable_2 = RunnableLambda(mul_two) # Convertendo a função de multiplicação para runnable

# Criando a cadeia sequencial
sequence = runnable_1 | runnable_2

resposta = sequence.invoke(5)

# print(runnable_1.invoke(1))
# print(runnable_2.invoke(1))

print("------ RESPOSTA DO INVOKE EXEMPLO 2 - RunnableSequence ----")
print(resposta)
print("-----------------------------------------------------------")
