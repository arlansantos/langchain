from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatOllama(model='llama3.1:8b', temperature=0.1)

## Criando a conversa. Lembrando que os ChatModels recebem como entrada uma lista de mensagem. Assim o LangChain automaticamente converte isso na estrutura que o modelo LLM precisa receber para responder.

# 1° Forma
# mensagens = [
#   SystemMessage(content='Você é um especialista em futebol'),
#   HumanMessage(content='Qual a jogadora que tem mais prêmios da FIFA THE BEST?'),
#   AIMessage(content='A jogadora brasileira Marta, ela foi eleita seis vezes a melhor jogadora do mundo pela FIFA.'),
#   HumanMessage(content='Quem o jogador considerado o melhor de todos os tempos da champions league?')
# ]

# 2° Forma
mensagens = [
  ('system','Você é um especialista em futebol'),
  ('user','Qual a jogadora que tem mais prêmios da FIFA THE BEST?'),
  ('assistant','Você é um especialista em futebol'),
  ('user','Quem o jogador considerado o melhor de todos os tempos da champions league?')
]

resposta = model.invoke(mensagens)

print("--------RESPOSTA AIMessage:---------")
print(resposta)
print("-------------------------------------")

print("--------RESPOSTA Somente Texto:------")
print(resposta.content)
print("-------------------------------------")