# tools/current_time_tool.py
from typing import Type
from datetime import datetime
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class TimeToolInput(BaseModel):
    """Input schema for CurrentTimeTool."""
    query: str = Field(..., description="The query asking for current time.")

class CurrentTimeTool(BaseTool):
    name: str = "current_time_tool"
    description: str = "Returns the current date and time in YYYY-MM-DD HH:MM:SS format."
    args_schema: Type[BaseModel] = TimeToolInput

    def _run(self, query: str) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
