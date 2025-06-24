from google.adk import Agent
from fabio.model import BASE_MODEL
from .prompt import prompt
from .tools import register_user_profile

user_profile_agent = Agent(
    name="user_profile_agent",
    description=(
        """
        Agente responsável por coletar o perfil pessoal do usuário (nome, idade, gênero, tipo corporal e preferências) 
        para personalizar sugestões de roupas.
        """
    ),
    model=BASE_MODEL,
    instruction=prompt,
    tools=[register_user_profile],
)