from graph_workflow import create_graph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage
from bedrockManagedApp import BedrockManagedApplication

checkpointer = MemorySaver()
# in_memory_store = InMemoryStore()
# Step 3: Create and configure the graph workflow with two nodes
graph = create_graph()
app = graph.compile(checkpointer=checkpointer)

# Step 4: Test with a sample query
query = "Hi, My name is Esha."
initial_state = {"messages": [HumanMessage(content="Hi, My Name is Esha!")]}
config = {"configurable": {"thread_id": "1"}}

print("****** Starting chat with our friendly Bot *************")
response = app.invoke(initial_state, config)
print("User:", initial_state["messages"][-1].content)
print("**********************************************************")
print("Response:", response["messages"][-1].content)

print("**********************************************************")
#print(app.get_state(config))

query = "Who am I?"
next_state = {"messages": [HumanMessage(content=query)]}
response = app.invoke(next_state, config)
print("User:", next_state["messages"][-1].content)
print("**********************************************************")
print("Response:", response["messages"][-1].content)

def lambda_handler(event, context):
    bedrock_managed_app = BedrockManagedApplication()
    response_data = bedrock_managed_app.invoke_application(event, context)
    return {
        "statusCode": 200,
        "body": response_data
    }


event = {
    "inputs": {"messages": [HumanMessage(content=query)]},
    "config": {"configurable": {"thread_id": "1"}}
}
print(lambda_handler(event, {}))
