from datetime import datetime
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

# Define State here (or import from main.py if you prefer)
class State(TypedDict):
    messages: Annotated[list, add_messages]

def get_current_time(state: State) -> State:
    """Get the current time and add it to the messages."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    state["messages"].append(f"Current time is: {current_time}")
    return state
