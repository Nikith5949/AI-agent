# from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor


ollm = OllamaLLM(model="llama3.2", request_timeout=30.0)

# print(ollm.invoke("Hi"))


def calculator_tool(input: str) -> str:
    try:
        return str(eval(input))
    except Exception as e:
        return f"Error: {e}"

print(f'calculator_tool -> {calculator_tool("3+2")}')
tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for mathematical calculations."
    )
]

# Define the prompt
prompt = PromptTemplate(
    input_variables=["input"],
    template="You are an assistant. Answer the following query: {input}"
)

custom_prompt = PromptTemplate(
    input_variables=["input"],
    template=(
        "You are a helpful assistant capable of using tools. Answer the following query:\n"
        "{input}\n"
        "Think step by step and use the tools available if needed. "
        "Stop once you have the final answer."
    )
)
llm_chain = prompt | ollm

# agent = initialize_agent(
#     tools=tools,
#     llm=llm_chain,
#     agent="zero-shot-react-description",  
#     verbose=True
# )

agent = initialize_agent(
    llm=llm_chain,  # Pass the LLMChain with the custom prompt
    tools=tools,
    agent_type="zero-shot-react-description",
    verbose=True
)
# Run the agent


while True:
    inp=input("\n please enter your query or q to exit \n->")
    if inp.lower()=="q":
        print("Goodbye")
        break
    try:
        response = agent.invoke({"input":{"user":inp}})
        print(response)
    except Exception as e:
        print(f"Error2: {e}")



