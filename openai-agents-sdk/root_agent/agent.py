from agents import Agent

# User Defined Instructions
from root_agent.prompt import ROOT_AGENT_INSTRUCTIONS
from root_agent.handoffs.time_agent.agent import time_agent

agent = Agent(
    name="Root_Agent",
    instructions=ROOT_AGENT_INSTRUCTIONS,
    model="gpt-4o",
    handoffs=[time_agent],
)