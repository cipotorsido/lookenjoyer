from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from fabio.model import BASE_MODEL
# from fabio.sub_agents.stock_collector_agent.agent import stock_collector_agent
# from fabio.sub_agents.deal_presenter_agent import deal_presenter_agent
from fabio.sub_agents.user_profile_agent.agent import user_profile_agent


from fabio.prompt import prompt


root_agent = Agent(
    name="Fabio",
    model=BASE_MODEL,
    description=(
        """
        Fabio é um assistente de moda que ajuda pessoas a escolherem 
        roupas adequadas para diferentes ocasiões, considerando informações pessoais, 
        tipo de evento, clima e ambiente. Ele conversa de forma empática, acessível e 
        adaptada ao estilo e necessidades de cada pessoa.
        """
    ),
    instruction=(prompt),
    tools=[
        AgentTool(agent=user_profile_agent),
        # AgentTool(agent=event_context_agent),
        # AgentTool(agent=look_recommender_agent),
        # AgentTool(agent=feedback_agent),
    ],
)