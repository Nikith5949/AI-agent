
from typing import Annotated
from typing_extensions import TypedDict
from langchain_ollama import OllamaLLM
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages:Annotated[list,add_messages]



ollm = OllamaLLM(model="llama3.2", request_timeout=30.0)
def chatbot_ollm(state:State):
    global ollm
    return({"messages":('ai',ollm.invoke(state["messages"]))})