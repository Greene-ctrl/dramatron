# Dramatron CLI and API

This project provides a terminal-based CLI and a FastAPI-based web API for the Dramatron story generation system.

## Installation

```bash
pip install -r requirements.txt
```

## Running the CLI

To run the interactive CLI:

```bash
export DRAMATRON_API_KEY="your_api_key"
python3 -m dramatron.cli.main --logline "A story about a robot and a human."
```

## Running the API

To start the FastAPI server:

```bash
uvicorn dramatron.api.main:app --reload
```

Then visit `http://localhost:8000/docs` for the interactive API documentation.
