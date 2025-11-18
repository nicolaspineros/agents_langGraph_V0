from langgraph.graph.message import MessagesState
from langchain_core.messages import AIMessage
from langchain.chat_models import init_chat_model
import random

llm = init_chat_model(model="gpt-4o-mini", temperature=1)
openai_vector_store_ids = ["vs_691c8eeb51988191bf2286f5cd54ffbb"]

file_search_tool = {
    "type": "file_search",
    "vector_store_ids": openai_vector_store_ids,
}

llm = llm.bind_tools([file_search_tool])

class State(MessagesState):
    customer_name: str
    my_age: int

def extractor(state: State):
    return {}

def conversation(state: State):
    new_state: State = {}
    if state.get("customer_name", None) is None:
        new_state["customer_name"] = "John"
    else:
        new_state["my_age"] = random.randint(20, 30)

    history = state["messages"]
    last_message = history[-1]
    ai_message = llm.invoke(last_message.text)
    new_state["messages"] = [ai_message]
    print(new_state)
    return new_state


from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("conversation", conversation)
builder.add_node("extractor", extractor)

builder.add_edge(START, "extractor")
builder.add_edge("extractor", "conversation")
builder.add_edge("conversation", END)

agent = builder.compile()