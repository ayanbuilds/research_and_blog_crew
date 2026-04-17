# 🔬 Research & Blog Crew

A **CrewAI-powered multi-agent system** that automatically researches any topic and produces a polished, reader-friendly blog post. Two specialized AI agents work together in a sequential pipeline — one generates a detailed research report, and the other transforms it into an engaging blog article.

---

## 🤖 How It Works

The crew runs two agents sequentially:

| Agent | Role | Output |
|---|---|---|
| **Report Generator** | Researches the topic in depth and produces a structured ~2000-word report covering latest facts and future trends | Internal report passed to the next agent |
| **Blog Writer** | Reads the report and rewrites it as a fun, simple, ~500-word blog post that anyone can understand | `blogs/blog.md` |

The final blog post is saved to the `blogs/` directory as `blog.md`.

---

## 📁 Project Structure

```
research_and_blog_crew/
├── blogs/                          # Generated blog output
│   └── blog.md
├── src/
│   └── research_and_blog_crew/
│       ├── config/
│       │   ├── agents.yaml         # Agent definitions (role, goal, backstory)
│       │   └── tasks.yaml          # Task definitions (description, expected output)
│       ├── crew.py                 # Crew assembly and orchestration
│       ├── main.py                 # Entry point — set your topic here
│       └── __init__.py
├── .env                            # API keys and model configuration
├── pyproject.toml                  # Project metadata and dependencies
└── README.md
```

---

## ⚙️ Prerequisites

- **Python** `>=3.10, <3.14`
- **[uv](https://docs.astral.sh/uv/)** — fast Python package manager
- A **[Groq](https://console.groq.com/) API Key** (free tier available) — or swap in any supported LLM provider

---

## 🚀 Setup & Run — Step by Step

### 1. Clone the repository

```bash
git clone https://github.com/your-username/research_and_blog_crew.git
cd research_and_blog_crew
```

### 2. Install `uv` (if not already installed)

```bash
pip install uv
```

### 3. Install project dependencies

```bash
crewai install
```

> This uses `uv` under the hood to create a virtual environment and install all dependencies defined in `pyproject.toml`.

### 4. Configure your API key

Create a `.env` file in the project root (or edit the existing one):

```env
MODEL=groq/llama-3.3-70b-versatile
GROQ_API_KEY=your_groq_api_key_here
```

> **Using a different LLM?** Replace `MODEL` with any provider supported by CrewAI, e.g.:
> - `openai/gpt-4o` → set `OPENAI_API_KEY`
> - `anthropic/claude-sonnet-4-20250514` → set `ANTHROPIC_API_KEY`
> - `google/gemini-2.0-flash` → set `GEMINI_API_KEY`

### 5. (Optional) Change the topic

Open `src/research_and_blog_crew/main.py` and update the `topic` input:

```python
inputs = {
    'topic': 'Your topic here',  # ← change this
}
```

### 6. Run the crew

```bash
crewai run
```

The crew will:
1. Generate a ~2000-word research report on the topic
2. Use that report to write a ~500-word blog post
3. Save the final blog to `blogs/blog.md`

---

## 📄 Output

After a successful run, open `blogs/blog.md` to read your generated blog post.

---

## 🛠️ Customization

| File | What to change |
|---|---|
| `config/agents.yaml` | Agent roles, goals, and backstories |
| `config/tasks.yaml` | Task descriptions and expected output format |
| `src/.../main.py` | Input topic passed to the crew |
| `src/.../crew.py` | Add tools, change the process, or add new agents |

---

## 📦 Dependencies

- [`crewai[litellm,tools]==1.14.1`](https://pypi.org/project/crewai/) — the core multi-agent orchestration framework

---

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)
- [Join the Discord](https://discord.com/invite/X4JWnZnxPb)
