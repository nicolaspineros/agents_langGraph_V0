from typing import Literal
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from src.agents.support.state import State
from src.agents.support.routes.intent.promt import SYSTEM_PROMPT

class RouteIntent(BaseModel):
    step: Literal["conversation", "booking"] = Field(
        'conversation', description="The next step in the routing process"
    )

llm = init_chat_model(model="gpt-4o-mini", temperature=0)
llm = llm.with_structured_output(RouteIntent)

def intent_route(state: State) -> Literal["conversation", "booking"]:
    history = state["messages"]
    schema = llm.invoke([("system", SYSTEM_PROMPT)] + history)
    if schema is not None and schema.step is not None:
        return schema.step
    return "conversation"  # por defecto