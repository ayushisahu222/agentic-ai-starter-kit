# OpenAI Agent SDK Starter Kit

A clean, modular starter kit for building AI agents using **OpenAI Agent SDK**

---

## 📁 Project Layout
```bash
openai-agents-sdk/
├── main.py                  # Entry point to run the root agent
├── pyproject.toml           # Project dependencies and configuration
├── uv.lock                  # Locked dependencies (used with uv or pip)
├── root_agent/
│   ├── __init__.py          # Module init
│   ├── agent.py             # Root agent logic
│   ├── prompt.py            # Prompt template for the root agent
│   └── tools.py             # Tools used by the root agent
├── handoffs/
│   └── time_agent/
│       ├── __init__.py      # Module init
│       ├── agent.py         # Sub-agent to handle time-related tasks
│       ├── prompt.py        # Prompt template for the time agent
│       └── tools.py         # Tools (e.g., get_current_time) used by time agent
└── README.md                # Project documentation
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
cd openai-agents-sdk
uv pip install -r pyproject.toml
```

### 3. Setup the OpenAI API Key
```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 4. Run the agent
```bash
python main.py
```

To read more about OpenAI Agent SDK, visit https://openai.github.io/openai-agents-python/
