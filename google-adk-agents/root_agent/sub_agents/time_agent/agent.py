import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# user defined imports
from .prompt import TIME_AGENT_PROMPT
from .tools import current_time

# Constants
GPT_MODEL = os.getenv("GPT_MODEL")
# GEMINI_MODEL = os.getenv("GEMINI_MODEL","gemini-2.0-flash-001")

get_time_agent = LlmAgent(
    model=LiteLlm(model=GPT_MODEL), #Replace LiteLlm(model=GPT_MODEL) with GEMINI_MODEL if using Gemini
    name="Get_Time_Agent",
    description="Gives user current time.",
    instruction=TIME_AGENT_PROMPT,
    tools=[current_time],
)
