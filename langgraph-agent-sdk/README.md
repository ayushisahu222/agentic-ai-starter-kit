# LangGrapg Agent SDK Starter Kit

A clean, modular starter kit for building AI agents using **LangGraph Agent SDK**

---

## 📁 Project Layout
```bash
LANGGRAPH-AGENT/                          
├── subgraph_agents/                  # Contains agent node logic
│   ├── __init__.py
│   └── get_current_time.py           # Tool to get current time
├── uv.lock
├── main.py                           # Main entry point to run the graph
├── pyproject.toml                    # Project metadata and dependencies  
├── time_agent_workflow.png           # Saved workflow image of the LangGraph      
└── README.md                         # Project documentation

```

---
## 🚀 Quickstart

### 1. Clone the repository and setup the environment

```bash
git clone https://github.com/ayushisahu222/agentic-ai-starter-kit.git
cd agentic-ai-starter-kit
```

### 2. Install dependencies using uv
```bash
uv venv 
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
cd langgraph-agent-sdk
uv pip install -r pyproject.toml
```

### 3. Run the agent
```bash
python main.py
```

To read more about LangGraph Agent SDK, visit https://langchain-ai.github.io/langgraph/tutorials/get-started/1-build-basic-chatbot/
