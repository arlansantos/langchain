from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel

""" Exemplo 3 - RunnableParallel """


def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

def mul_three(x: int) -> int:
    return x * 3

runnable_1 = RunnableLambda(add_one) # Convertendo a função de soma para runnable
runnable_2 = RunnableLambda(mul_two) # Convertendo a função de multiplicação por 2 para runnable
runnable_3 = RunnableLambda(mul_three) # Convertendo a função de multiplicação por 3 para runnable

sequence = runnable_1 | {  # o dicionário aqui é entendido como 'RunnableParallel'
    "mul_two": runnable_2,
    "mul_three": runnable_3,
}

# Ou usando o equivalente:
# sequence = runnable_1 | RunnableParallel(
#     {"mul_two": runnable_2, "mul_three": runnable_3}
# )

# Ou também o equivalente:
# sequence = runnable_1 | RunnableParallel(
#     mul_two=runnable_2,
#     mul_three=runnable_3,
# )

# Também posso paralelizar no inicio:
# sequence = RunnableParallel(
#     mul_two=runnable_2,
#     mul_three=runnable_3,
# )

resposta = sequence.invoke(5)

print("------ RESPOSTA DO INVOKE EXEMPLO 3 - RunnableParallel ----")
print(resposta)
print("-----------------------------------------------------------")
