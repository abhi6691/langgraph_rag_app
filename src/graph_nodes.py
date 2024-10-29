from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

class RetrieveNode(Runnable):
    def __init__(self, retriever):
        self.retriever = retriever

    def invoke(self, input, config, **kwargs):
        query = input.get("query")
        retrieved_docs = self.retriever.get_relevant_documents(query)
        return {"documents": retrieved_docs, "query": query}

class GenerateAnswerNode(Runnable):
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo",
                          api_key="sk-*")

    def invoke(self, input, config, **kwargs):
        query = input.get("query")
        prompt = f"Answer the question '{query}'"
        # print(prompt)

        # Wrap prompt in a HumanMessage for the chat model
        answer = self.llm.invoke([HumanMessage(content=prompt)])
        return {"messages": answer.content}
