# AI Agent

A command-line AI coding agent powered by **Google Gemini 2.5 Flash**. Give it a prompt and it autonomously plans and executes multi-step tasks on your local codebase — reading files, writing code, running scripts, and verifying tests — all through a function-calling loop.

---

## How It Works

The agent runs an agentic loop (up to 20 iterations) where it:

1. Receives your prompt as a command-line argument
2. Calls Gemini 2.5 Flash with a set of available tools
3. Executes whichever tool(s) the model requests
4. Feeds the results back to the model
5. Repeats until the model produces a final answer or tests pass

---

## Available Tools

The agent can perform the following operations on your working directory:

| Tool | Description |
|---|---|
| `get_files_info` | List files and directories |
| `get_file_content` | Read the contents of a file |
| `run_python_file` | Execute a Python file with optional arguments |
| `write_file` | Write or overwrite a file |
| `run_python_file` (tests) | Run `tests.py` and stop if all tests pass |

All file paths are relative to the working directory. The working directory is injected automatically for security.

---

## Project Structure

```
aiagent/
├── main.py               # CLI entry point and agent loop
├── call_function.py      # Dispatches tool calls from the model
├── prompts.py            # System prompt defining agent behaviour
├── config.py             # Configuration (reserved)
├── functions/            # Tool implementations
├── calculator/           # Example project for the agent to work on
├── test_get_file_content.py
├── test_get_files_info.py
├── test_run_python_file.py
├── test_write_file.py
└── pyproject.toml
```

---

## Requirements

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

---

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/cjawale-QABA/aiagent.git
   cd aiagent
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Configure your API key**

   Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

---

## Usage

```bash
uv run main.py "<your prompt>"
```

To enable verbose output (shows each tool call result as it happens):

```bash
uv run main.py "<your prompt>" --verbose
```

### Examples

```bash
# Ask the agent to explain the project
uv run main.py "What does this project do?"

# Ask the agent to fix a bug
uv run main.py "Fix the failing tests in the calculator module"

# Ask the agent to add a feature
uv run main.py "Add a subtract function to the calculator and write a test for it"
```

---

## Dependencies

| Package | Version |
|---|---|
| `google-genai` | 1.12.1 |
| `python-dotenv` | 1.1.0 |

---

## Running Tests

The test files can be run individually with `uv run` or all at once:

```bash
uv run test_get_file_content.py
uv run test_get_files_info.py
uv run test_run_python_file.py
uv run test_write_file.py
```
