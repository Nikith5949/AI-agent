from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages

from typing_extensions import TypedDict
from typing import Annotated
from lang_graph_age1 import chatbot_ollm,State
from IPython.display import Image, display

# class State(TypedDict):
#     messages:Annotated[list,add_messages]


graph_builder=StateGraph(State)
graph_builder.add_node("node_cb",chatbot_ollm)
# graph_builder.add_node("node_cb1",chatbot_ollm)
graph_builder.add_edge(START,"node_cb")
graph_builder.add_edge("node_cb",END)

graph=graph_builder.compile()


# generate an image of the graph
def generate_graph_img(graph):
    try:
        # display(Image(graph.get_graph().draw_mermaid_png()))

        with open("graph.png", "wb") as f:
            f.write(graph.get_graph().draw_mermaid_png())

    except Exception as e:
        print(f'Error display graph->{e}')

generate_graph_img(graph)



# user input

while True:
    inp=input("\n please enter your query or q to exit \n->")
    if inp.lower()=="q":
        print("Goodbye")
        break
    try:
        print(graph.stream({'messages':("user",inp)}))
        print("------")
        for event in graph.stream({'messages':inp}):
            print(event)
        
        print(graph.messages)
            # print(f"\n total -> {graph.get_state()['messages']}")
    except Exception as e:
        print(f"Error2: {e}")

