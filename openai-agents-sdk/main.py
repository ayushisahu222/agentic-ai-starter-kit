import asyncio
from agents import Runner, trace

#User Defined Imports
from root_agent.agent import agent

async def main():
    with trace("OpenAI Agents SDK Starter Kit"):
        result = await Runner.run(agent, "Give me the current time.")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
