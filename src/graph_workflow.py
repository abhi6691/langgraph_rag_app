from langgraph.graph import END, StateGraph, START, MessagesState
from graph_nodes import RetrieveNode, GenerateAnswerNode
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def create_graph():
    graph = StateGraph(MessagesState)

    def call_generate_node(state: MessagesState):
        messages = state['messages']
        llm = ChatOpenAI(model="gpt-3.5-turbo",
                        api_key = "sk-*")
        answer = llm.invoke(messages)
        return {"messages": answer}
    
    graph.add_node("generate", call_generate_node)

    graph.add_edge("generate", END)
    graph.add_edge(START, "generate")
    return graph
