# pip install langchain-groq => precisa instalar
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import ollama

load_dotenv()

model = ChatOllama(model = "llama3.1:8b")

resposta = model.invoke(["Olá como você está e o que você é capaz de fazer?"])

print("--------RESPOSTA AIMessage:---------")
print(resposta)
print("-------------------------------------")

print("--------RESPOSTA Somente Texto:------")
print(resposta.content)
print("-------------------------------------")

# response = ollama.chat(model='deepseek-r1:7b', messages=[{'role': 'user', 'content': 'Olá como você está e o que você é capaz de fazer?'}])
# print(response['message']['content'])


# response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': 'Olá como você está e o que você é capaz de fazer?'}])
# print(response['message']['content'])