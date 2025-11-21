# Text Chunker Script

This Python script reads large text documents from a JSON file, splits the text into smaller chunks suitable for embedding and vector search using the `tiktoken` library, preserves metadata, and outputs a new JSON file with the chunked data.

## Requirements

- Python 3.7+
- `tiktoken` library

## Installation

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the input JSON file and output JSON file paths:

```bash
python text_chunker.py input.json output.json
```

### Input JSON Format

The input JSON file should be a list of objects, each containing at least a `text` field and any additional metadata fields. Example:

```json
[
  {
    "id": "doc1",
    "date": "2025-11-21",
    "sender": "user@example.com",
    "text": "Long text content here..."
  },
  {
    "id": "doc2",
    "date": "2025-11-20",
    "sender": "another@example.com",
    "text": "Another long text content..."
  }
]
```

### Output JSON Format

The output JSON file will contain the chunked text with preserved metadata and an added `chunk_index` field indicating the chunk number. Example:

```json
[
  {
    "id": "doc1",
    "date": "2025-11-21",
    "sender": "user@example.com",
    "text": "Chunk 0 text...",
    "chunk_index": 0
  },
  {
    "id": "doc1",
    "date": "2025-11-21",
    "sender": "user@example.com",
    "text": "Chunk 1 text...",
    "chunk_index": 1
  }
]
```
