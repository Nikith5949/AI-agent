# from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM



llm = OllamaLLM(model="llama3.2", request_timeout=30.0)

print(llm.invoke("Hi"))


