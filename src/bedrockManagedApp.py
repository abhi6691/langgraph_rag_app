from graph_workflow import create_graph
from langgraph.checkpoint.memory import MemorySaver

class BedrockManagedApplication:
    def __init__(self):
        # This constructor does not accept any parameters
        self.checkpointer = MemorySaver()

    def __new__(cls, *args, **kwargs):
        if args or kwargs:
            raise TypeError("This class does not accept parameters in the constructor.")
        return super().__new__(cls)
        
    
    def initialize():
        pass
    
    def destroy():
        pass
        
    def invoke_application(self, event, context):
        graph = create_graph()
        app = graph.compile(checkpointer=self.checkpointer)

        inputs = event.get("inputs", {})
        config = event.get("config", {})

        response = app.invoke(inputs, config)
        return response