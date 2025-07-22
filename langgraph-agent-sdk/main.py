import os
from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages

# Import your node function
from subgraph_agents.get_current_time import get_current_time

# Optional: save graph image to file
def save_graph_image(graph, filename="time_agent_workflow.png"):
    graph_dot = graph.get_graph().draw_mermaid_png()
    with open(filename, "wb") as f:
        f.write(graph_dot)
    print(f"✅ Workflow image saved as: {filename}")

# --- Define State ---
class State(TypedDict):
    messages: Annotated[list, add_messages]

# --- Build the graph ---
def build_time_agent():
    builder = StateGraph(State)

    builder.add_node("get_time", get_current_time)
    builder.set_entry_point("get_time")
    builder.set_finish_point("get_time")

    return builder.compile()

# --- Run ---
def main():
    graph = build_time_agent()

    # Optional: save workflow image
    save_graph_image(graph)

    input_state = {"messages": []}
    final_state = graph.invoke(input_state)

    print("\n🕒 Final Messages:")
    for msg in final_state["messages"]:
        print(f"→ {msg}")

if __name__ == "__main__":
    main()

