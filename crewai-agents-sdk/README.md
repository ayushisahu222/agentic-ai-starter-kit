# CrewAI Agent SDK Starter Kit

A clean, modular starter kit for building AI agents using **CrewAI Agent SDK**

---

## 📁 Project Layout
```bash
crewai-agents-sdk/
├── pyproject.toml              # Project and dependency config
├── uv.lock
├── src/
│   └── agents_crew/            # Your CrewAI project module
│       ├── __init__.py
│       ├── main.py             # Entrypoint (run this)
│       ├── crew.py             # CrewBase class and all agents/tasks
│       ├── config/             # Agent and task definitions (YAML)
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── tools/              # Custom tools
│           ├── __init__.py
│           └── current_time_tool.py
└── README.md 
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
cd crewai-agents-sdk
uv pip install -r pyproject.toml
```

### 3. Setup the OpenAI API Key
```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
Go to https://platform.openai.com/docs/overview to get the OpenAI API key.

### 4. Run the agent
```bash
cd src/agents_crew
python main.py
```

To read more about CrewAI Agent SDK, visit https://docs.crewai.com/en/guides/crews/first-crew
