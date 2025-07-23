# src/research_crew/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# User-defined imports
from tools.current_time_tool import CurrentTimeTool

@CrewBase
class TimeCrew():
    """Time crew for providing accurate and up-to-date time information"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def time_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['time_agent'],  # type: ignore[index]
            verbose=True,
            tools=[CurrentTimeTool()]
        )

    @task
    def get_time(self) -> Task:
        return Task(
            config=self.tasks_config['time_task'] # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the time crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )