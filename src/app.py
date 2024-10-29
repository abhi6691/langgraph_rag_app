from graph_workflow import create_graph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage

checkpointer = MemorySaver()
in_memory_store = InMemoryStore()
# Step 3: Create and configure the graph workflow with two nodes
graph = create_graph()
app = graph.compile(checkpointer=checkpointer, store=in_memory_store)

# Step 4: Test with a sample query
query = "Hi, My name is Esha."
initial_state = {"messages": [HumanMessage(content="Hi, My Name is Esha!")]}
config = {"configurable": {"thread_id": "1"}}
response = app.invoke(
    {"messages": [HumanMessage(content="Hi, My Name is Esha!")]},
    config={"configurable": {"thread_id": "1"}}
)
print(initial_state)
print("**********************************************************")
print("Response:", response["messages"][-1].content)

print("**********************************************************")
#print(app.get_state(config))

query = "Hello, who am I? What is my name?"
next_state = {"messages": [HumanMessage(content=query)]}
response = app.invoke(next_state, config)
print(next_state)
print("**********************************************************")
print("Response:", response["messages"][-1].content)
