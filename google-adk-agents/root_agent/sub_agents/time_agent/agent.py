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
GPT_MODEL = os.getenv("GPT_MODEL", "openai/gpt-4o")

get_time_agent = LlmAgent(
    model=LiteLlm(model=GPT_MODEL),
    name="Get_Time_Agent",
    description="Gives user current time.",
    instruction=TIME_AGENT_PROMPT,
    tools=[current_time],
)