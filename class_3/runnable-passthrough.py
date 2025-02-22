from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel

""" Exemplo 4 - RunnablePassthrough """


# chain = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough ()

# # Independente de quantas vezes você "passar o resultado para frente", a entrada não é alterada.

# resposta = chain.invoke("Olá")


# print("------ RESPOSTA DO INVOKE EXEMPLO 4 - RunnablePassthrough -")
# print(resposta)
# print("-----------------------------------------------------------")

""" Exemplo 5 - RunnablePassthrough + RunnableLambda """


# def entrada_para_letras_maiusculas(entrada: str):
#     saida = entrada.upper()
#     return saida

# chain = RunnablePassthrough() | RunnableLambda(entrada_para_letras_maiusculas) | RunnablePassthrough()

# # Neste caso vamos receber a entrada do usuário, passar para a função 'entrada_para_letras_maiusculas', transformar olá -> OLÁ e passar para frente.

# resposta = chain.invoke("olá")



# print("------ RESPOSTA DO INVOKE EXEMPLO 5 - RunnablePassthrough + RunnableLambda  -")
# print(resposta)
# print("-----------------------------------------------------------------------------")

# ====================================================================================================================

""" Exemplo 6 - Operador Assign """

# https://python.langchain.com/docs/how_to/assign/

# Pego a entrada e passo para frente e na segunda etapa, eu antes de passar para frente eu adiciono uma chave
# 'multiplica_3' no dicionário de entrada multiplicando a antrada original por 3

runnable = RunnablePassthrough() | RunnablePassthrough.assign(multiplica_3=lambda x: x["num"] * 3)

resposta = runnable.invoke({"num": 1})

print("------ RESPOSTA DO INVOKE EXEMPLO 6 - Operador Assign -----------------------")
print(resposta)
print("-----------------------------------------------------------------------------")