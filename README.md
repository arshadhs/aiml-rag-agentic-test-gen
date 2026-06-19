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