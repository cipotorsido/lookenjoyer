from google.adk import Agent

from fabio.agent import BASE_MODEL
from .prompt import prompt
from .tools import look_generator_tool

look_recommender_agent = Agent(
    name="look_recommender_agent",
    model=BASE_MODEL,
    instruction=prompt,
    tools=[look_generator_tool]
)