# AIML RAG Agentic Test Generator

This project explores how Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and agentic AI workflows can be used to generate software test cases from requirements, source code, documentation, and existing tests.

The system retrieves relevant project context, plans test scenarios, generates executable tests, reviews them, runs them, and reports coverage and quality metrics.

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

On Mac/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

You can copy the structure:

```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_DB_PATH=./chroma_db
```

Note: Do not commit your real `.env` file to GitHub.

# Planned Structure
```

- app/main.py  = starts and runs the workflow
- agents/      = future agent logic
- rag/         = RAG loading, splitting, vector store, retrieval
- data/        = input documents
- generated_tests/ = AI-generated test files
- evaluation/  = coverage and quality metrics

aiml-multi-agent-test-generator/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── pipeline.py
│
├── agents/
│   ├── requirement_agent.py
│   ├── code_analysis_agent.py
│   ├── test_planner_agent.py
│   ├── test_generator_agent.py
│   ├── test_reviewer_agent.py
│   └── report_agent.py
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── vector_store.py
│   └── retriever.py
│
├── └── data/
│   ├── requirements/
│   │   └── requirements.md
│   ├── docs/
│	│   └── api_spec.md
│   ├── existing_tests/
│   │   └── existing_tests.md
│   └── source_code/
│       └── source_code.md
│
├── generated_tests/
│
├── evaluation/
│   ├── coverage_report.py
│   └── metrics.py
│
├── notebooks/
│
└── tests/
```