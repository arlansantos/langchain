from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel

""" Desafio com Runnables:

Processo:

1) Receber a entrada do tipo {"input": "Parabéns Você"}  e passar para frente (testar uso do RunnablePassthrough)

2) Quando eu receber a entrada de (1) eu gostaria de criar um dicionário mantendo a entrada de (1) intacta, mas criando 
uma chave nova ("num_caract") tal que seja a entrada de (1) contando o total de caracteres.

3) Usando a saída de (2) quero paralelizar a entrada em dois processos, o primeiro, pegando a entrada textual e 
adicionando a palavra " Conseguiu!" numa chave chamada "transformar_entrada" o segundo não farei nada, apenas passarei 
para frente a entrada sem qualquer alteração numa chave "passa_para_frente".

4) Por fim, vou passar para frente a combinação do processo paralelo e imprimir o resultado.

"""

def contar_caracteres(entrada: dict):
    entrada["num_caract"] = len(entrada["input"])
    return entrada

def transformar_entrada(entrada: dict):
    entrada["input"] += " Conseguiu!"
    return entrada

def passa_para_frente(entrada: dict):
    return entrada

chain = RunnablePassthrough() | RunnableLambda(contar_caracteres) | RunnableParallel(
    transformar_entrada=RunnableLambda(transformar_entrada),
    passa_para_frente=RunnableLambda(passa_para_frente) 
) | RunnablePassthrough()

resposta = chain.invoke({"input": "Parabéns Você"})
print(resposta)