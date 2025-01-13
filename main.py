from llama_index.llms.ollama import Ollama



ollm = Ollama(
    model="llama3.2",
    request_timeout=30.0
)

response = ollm.complete("hello")
print(response)

