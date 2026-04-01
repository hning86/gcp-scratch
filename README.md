# test02

A collection of Python scripts demonstrating various Google Cloud services, including Generative AI and Natural Language processing.

## Scripts Overview

### `flash-lite.py`
This script uses the `google-genai` library to interact with the `gemini-3.1-flash-lite-preview` model. It is configured to:
- Generate summaries based on a user's prompt (e.g., "summarize the events from yesterday").
- Utilize **Google Search** as a tool for enhanced information retrieval.
- Use **Vertex AI** for model execution.
- Include custom safety settings and thinking configuration.

### `ner.py`
This script demonstrates Named Entity Recognition (NER) using the `google-cloud-language` API. It:
- Analyzes text content for entities such as persons, locations, and organizations.
- Outputs representative names, entity types, salience scores, and metadata (like Wikipedia URLs).
- Detects mentions of entities within the text.

## Prerequisites

1.  **Google Cloud Project:** You must have a Google Cloud project with the Vertex AI and Natural Language APIs enabled.
2.  **Authentication:** Set up your application default credentials (ADC) to authenticate with Google Cloud.
    ```bash
    gcloud auth application-default login
    ```
3.  **Project ID:** Update the `project` ID in `flash-lite.py` to match your Google Cloud project.

## Installation

This project uses `uv` for package management. To install the dependencies, run:

```bash
uv sync
```

## Usage

### Run Gemini Flash Lite Script
To execute the generative AI summary:
```bash
uv run flash-lite.py
```

### Run Named Entity Recognition Script
To execute the NER analysis:
```bash
uv run ner.py
```

## Dependencies
- `google-cloud-language`: For natural language processing and entity recognition.
- `google-genai`: For interacting with Google's generative models.
- `pyopenssl`: For secure network communications.
