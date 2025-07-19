from agents import Agent
from agents.model_settings import ModelSettings

# User Defined Instructions
from root_agent.handoffs.time_agent.prompt import TIME_AGENT_INSTRUCTIONS
from root_agent.handoffs.time_agent.tools import get_current_time

time_agent = Agent(
    name="Time_Agent",
    instructions=TIME_AGENT_INSTRUCTIONS,
    model="gpt-4o",
    tools=[get_current_time],
    model_settings=ModelSettings(tool_choice="required"), 
)