from document_loader import load_and_split_document
from vector_store import setup_vector_store
from graph_workflow import create_graph

# Step 1: Load and prepare document chunks
chunks = load_and_split_document()

# Step 2: Set up the vector store and retrieval function
retriever = setup_vector_store(chunks)

# Step 3: Create and configure the graph workflow with two nodes
graph = create_graph(retriever)
app = graph.compile()

# Step 4: Test with a sample query
query = "What is the InvokeAgent request syntax?"
initial_state = {"query": query}
response = app.invoke(initial_state)
print("**********************************************************")
print("Response:", response["answer"])
