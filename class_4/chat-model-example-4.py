from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import asyncio

load_dotenv()
async def conversa_com_modelo():
  model = ChatOllama(model='llama3.1:8b', temperature=0.1)

  conversa = [SystemMessage(content="Você é um assistente útil que responde ao usuário com detalhes e exemplos.")]

  while(True):
    entrada = input('\n\nDigite aqui para conversa, caso queira encerrar digite: "-1": ')

    if(entrada == '-1'):
      break

    conversa.append(HumanMessage(content=entrada))

    all_chunk = []  
    async for chunk in model.astream(conversa):  
        all_chunk.append(chunk.content)  
        print(chunk.content, end="", flush=True) 

    resposta_completa = "".join(all_chunk)  
    conversa.append(AIMessage(content=resposta_completa))

  print("---- Histórico Completo ----")
  print(conversa)

asyncio.run(conversa_com_modelo())