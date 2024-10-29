from document_loader import load_and_split_document
from vector_store import setup_vector_store
from graph_workflow import create_graph

class ECSInitializer:
    def __init__(self):
        self.vector_store = None
        self.setup_vector_store()

    def setup_vector_store(self):
        if self.vector_store is None:
            # Initialization logic to be run only once at ECS startup
            chunks = load_and_split_document()
            self.vector_store = setup_vector_store(chunks)

    def get_retriever(self):
        return self.vector_store

# Main processing function that uses the initialized vector store
def process_query(query, retriever):
    graph = create_graph(retriever)
    initial_state = {"query": query}
    app = graph.compile()
    return app.invoke(initial_state)

def main():
    ecs_initializer = ECSInitializer()
    query = input("Enter your query: ")
    retriever = ecs_initializer.get_retriever()
    response = process_query(query, retriever)
    print("Response:", response)

if __name__ == "__main__":
    main()
