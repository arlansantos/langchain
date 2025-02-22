from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatOllama(model='llama3.1:8b', temperature=0.1)

conversa = [SystemMessage(content="Você é um assistente útil que responde ao usuário com detalhes e exemplos.")]

while(True):
  entrada = input('\n\nDigite aqui para conversa, caso queira encerrar digite: "-1": ')

  if(entrada == '-1'):
    break

  conversa.append(HumanMessage(content=entrada))

  resultado = model.invoke(conversa)
  resposta = resultado.content

  conversa.append(AIMessage(content=resposta))

  print(f'Resposta da IA: {resposta}')

print("---- Histórico Completo ----")
print(conversa)