import os
import logging

# Import necessary modules from google-adk
from google.genai import types
from google.adk.runners import Runner
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configure logging (basic setup)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User Defined Imports 
from root_agent.sub_agents.time_agent.agent import get_time_agent 
from root_agent.prompt import ROOT_AGENT_PROMPT

# Constants
GPT_MODEL = os.getenv("GPT_MODEL")
# GEMINI_MODEL = os.getenv("GEMINI_MODEL","gemini-2.0-flash-001")

root_agent = LlmAgent(
    model=LiteLlm(model=GPT_MODEL), #Replace LiteLlm(model=GPT_MODEL) with GEMINI_MODEL if using Gemini
    name="Root_Agent",
    description="This is your orchestrator agent. It manages other agents and tools. Make sure to you write a good description for it.",
    instruction=ROOT_AGENT_PROMPT,
    sub_agents=[get_time_agent],
)

