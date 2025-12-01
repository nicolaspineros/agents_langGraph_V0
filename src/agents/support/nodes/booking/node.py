from langchain.agents import create_agent
from src.agents.support.nodes.booking.tools import tools
from src.agents.support.nodes.booking.promt import prompt_template

booking_node = create_agent(
    model="openai:gpt-4o-mini",
    tools=tools,
    system_prompt=prompt_template.format(),
)