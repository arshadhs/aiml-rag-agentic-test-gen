# AIML RAG Agentic Test Generator

This project explores how **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, and future **agentic AI workflows** can be used to generate software test cases from requirements, source code, documentation, and existing tests.

The current MVP loads project documents, retrieves relevant context, generates pytest test cases using an LLM, saves the generated tests, and allows them to be executed against real application code.

---

## Project Status

Current MVP:

* Loads documents from the `data/` folder
* Splits documents into smaller chunks
* Creates embeddings using OpenAI
* Performs similarity-based retrieval
* Sends retrieved context to the LLM
* Generates pytest test cases
* Saves generated tests into `generated_tests/python/`
* Runs generated tests using pytest
* Supports coverage reporting

Planned future improvements:

* Multi-agent workflow
* Test review agent
* Test execution agent
* Coverage analysis agent
* Report generation agent
* ChromaDB or persistent vector database support
* C++ / GoogleTest support

---

## Current Project Flow

```text
data/
    ↓
RAG loader
    ↓
Text splitter
    ↓
Embeddings and vector store
    ↓
Context retrieval
    ↓
LLM test generation
    ↓
generated_tests/python/
    ↓
pytest execution
    ↓
coverage report
```

---

## Installation

### 1. Create a virtual environment

From the project root:

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

On Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bash
.venv\Scripts\activate.bat
```

On Mac/Linux:

```bash
source .venv/bin/activate
```

After activation, your terminal should show:

```bash
(.venv)
```

### 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

You can copy the structure from `.env.example`:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_DB_PATH=./chroma_db
```

Do not commit your real `.env` file to GitHub.

Your `.gitignore` should include:

```gitignore
.venv/
.env
__pycache__/
.pytest_cache/
.coverage
htmlcov/
chroma_db/
```

---

## How to Run the RAG Test Generator

From the project root:

```bash
python -u app/main.py
```

On Windows, this also works:

```bash
python -u app\main.py
```

The script will:

1. Load documents from `data/`
2. Split the documents into chunks
3. Create embeddings
4. Retrieve relevant context
5. Generate pytest test cases using the LLM
6. Save generated tests into:

```text
generated_tests/python/test_auth_service_generated.py
```

---

## Running the Generated Tests

After generating the test file, run:

```bash
python -m pytest generated_tests/python/test_auth_service_generated.py -v
```

On Windows:

```bash
python -m pytest generated_tests\python\test_auth_service_generated.py -v
```

The generated tests should execute against the real application code in:

```text
app/auth_service.py
```

---

## Running Test Coverage

To run tests with coverage:

```bash
python -m coverage run -m pytest generated_tests/python/test_auth_service_generated.py
python -m coverage report
```

On Windows:

```bash
python -m coverage run -m pytest generated_tests\python\test_auth_service_generated.py
python -m coverage report
```

Optional HTML coverage report:

```bash
python -m coverage html
```

Then open:

```text
htmlcov/index.html
```

---

## Current Folder Structure

```text
aiml-rag-agentic-test-gen/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── auth_service.py
│
├── agents/
│   ├── requirement_agent.py
│   ├── code_analysis_agent.py
│   ├── test_planner_agent.py
│   ├── test_generator_agent.py
│   ├── test_reviewer_agent.py
│   └── report_agent.py
├── rag/
│   ├── __init__.py
│   ├── loader.py
│   ├── splitter.py
│   ├── vector_store.py
│   └── retriever.py
│
├── data/
│   ├── requirements/
│   │   └── requirements.md
│   │
│   ├── docs/
│   │   └── api_spec.md
│   │
│   ├── existing_tests/
│   │   └── existing_tests.md
│   │
│   └── source_code/
│       └── source_code.md
│
├── generated_tests/
│   └── python/
│       └── test_auth_service_generated.py
│
├── agents/
│   └── README.md
│
├── evaluation/
│   ├── coverage_report.py
│   └── metrics.py
│
├── notebooks/
│
└── tests/
```

---

## Folders

| Folder             | Purpose                                                                         |
| ------------------ | ------------------------------------------------------------------------------- |
| `app/`             | Main Python application and real code under test                                |
| `rag/`             | RAG helper modules for loading, splitting, retrieval, and vector store creation |
| `data/`            | Input documents used by the RAG system                                          |
| `generated_tests/` | AI-generated test files                                                         |
| `agents/`          | Future multi-agent logic                                                        |
| `evaluation/`      | Future coverage and test quality metrics                                        |
| `tests/`           | Manually written project tests                                                  |
| `notebooks/`       | Experiments and analysis notebooks                                              |

---

## Important Concept

There is a difference between the **real code under test** and the **RAG input documents**.

Example:

```text
app/auth_service.py
```

This is the real Python code that pytest executes.

```text
data/source_code/source_code.md
```

This is the source-code context that the RAG system reads.

For the MVP, both may describe the same logic. Later, the loader can be improved to read real `.py`, `.cpp`, `.h`, or `.hpp` files directly.

---

## Example Full Windows Command Flow

```bash
cd C:\gitHub\aiml-rag-agentic-test-gen

python -m venv .venv
.venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python -u app\main.py

python -m pytest generated_tests\python\test_auth_service_generated.py -v

python -m coverage run -m pytest generated_tests\python\test_auth_service_generated.py
python -m coverage report
```

---

## Future Agentic AI Design

The planned multi-agent version may include:

| Agent                | Responsibility                             |
| -------------------- | ------------------------------------------ |
| Requirement Agent    | Reads requirements and acceptance criteria |
| Code Analysis Agent  | Understands functions, classes, and logic  |
| Test Planner Agent   | Decides what tests should be generated     |
| Test Generator Agent | Generates test cases                       |
| Test Reviewer Agent  | Checks generated tests for quality         |
| Test Executor Agent  | Runs pytest or GoogleTest                  |
| Report Agent         | Summarises coverage and test quality       |

---
