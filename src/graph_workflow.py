from langgraph.graph import END, Graph
from graph_nodes import RetrieveNode, GenerateAnswerNode

def create_graph(retriever):
    graph = Graph()
    retrieve_node = RetrieveNode(retriever)
    generate_node = GenerateAnswerNode()
    
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)

    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    graph.set_entry_point("retrieve")
    
    return graph
