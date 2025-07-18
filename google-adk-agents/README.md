# Google ADK Starter Kit

A clean, modular starter kit for building AI agents using **Google ADK** + **LiteLLM**.

Supports two modes:
1. 🌐 **GUI Mode** via `adk web`
2. 🖥️ **Script Mode** via `main.py`

---

## 📁 Project Layout
```bash
google-adk-agents/
├── .env # Environment config (.env)
├── main.py # Script entrypoint
├── pyproject.toml # Dependency declarations
├── uv.lock # Locked dependency versions
├── root_agent/
│ ├── agent.py # Root LlmAgent orchestrator
│ ├── prompt.py # Root agent prompt messages
│ └── sub_agents/
│ └── time_agent/
    │ ├── agent.py # Sub-agent to return current time
    │ ├── prompt.py # Sub-agent prompt
    │ └── tools.py # Sub-agent tools (if any)
└── README.md # This file
```

---
## 🚀 Quickstart

### 1. Clone the repository and setup the environment

```bash
git clone https://github.com/<your-user>/agentic-ai-starter-kit.git
cd agentic-ai-starter-kit
```

### 2. Install dependencies using uv
```bash
uv venv 
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
```

### 3. Change the name of the file dotenv.exmaple -> .env
```bash
GPT_MODEL=openai/gpt-4o
OPENAI_API_KEY=sk-xxxxxxx
```

### 4. Run the agent
Note: Make sure in the right directory.

A. Script Mode
```bash
python main.py
```
B. GUI Mode with ADK
```bash
adk web
```
Visit http://localhost:8080 to interact.

To read more about Google ADK, visit https://google.github.io/adk-docs/
