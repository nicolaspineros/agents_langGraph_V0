from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from src.agents.support.state import State

from src.agents.support.nodes.extractor.promt import SYSTEM_PROMPT

class ContactInfo(BaseModel):
    name: str = Field(description="The name of the person")
    phone: str = Field(description="The phone number of the person")
    email: str = Field(description="The email of the person")    
    age: str = Field(description="The age of the person")

llm = init_chat_model(model="gpt-4o-mini", temperature=0)
llm = llm.with_structured_output(ContactInfo)

def extractor(state: State):
    history = state["messages"]
    customer_name = state.get("customer_name", None)
    new_state: State = {}
    if customer_name is None or len(history) > 10:
        schema = llm.invoke([("system", SYSTEM_PROMPT)] + history)
        new_state["customer_name"] = schema.name
        new_state["phone"] = schema.phone    
        new_state["my_age"] = schema.age
    return new_state