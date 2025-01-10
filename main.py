from llama_index.llms.ollama import Ollama


llm = Ollama(
    model="llama3.2",
    request_timeout=30.0
)

response = llm.complete("hello")
print(response)