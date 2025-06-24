from google.adk import Agent

from fabio.model import BASE_MODEL
from .prompt import prompt
from .tools import event_context_tool

event_context_agent = Agent(
    name="event_context_agent",
    model=BASE_MODEL,
    instruction=prompt,
    tools=[event_context_tool],
)