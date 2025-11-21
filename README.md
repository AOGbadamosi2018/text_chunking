# Data Processing Pipeline for ACE the Data Science Interview

This project processes the "Ace the Data Science Interview" book content into a structured format suitable for further analysis, embedding, or search applications.

## Data Processing Pipeline

### Input Format (`ace_the_data.json`)
- **Structure**: Array of objects
- **Fields per object**:
  - `page_number`: Integer indicating the page number
  - `content`: String containing the full text of the page

### Output Format (`ace_data_chunks.json`)
- **Structure**: Array of chunked content objects
- **Fields per chunk**:
  - `id`: Unique identifier for the page (e.g., "ace_data_page_1")
  - `date`: Processing date in YYYY-MM-DD format
  - `page_number`: Original page number from the input
  - `text`: Chunk of text (around 1000 tokens)
  - `chunk_index`: Index of the chunk within its page (0-based)
  - `total_chunks`: Total number of chunks for this page

### Key Transformations
1. **Chunking**: Long pages are split into smaller, manageable chunks of approximately 1000 tokens each
2. **Metadata Enrichment**: Added processing date and chunking information
3. **Empty Page Handling**: Empty pages are filtered out
4. **Consistent Structure**: Each chunk follows the same structure for easier processing

### Example Transformation

**Input:**
```json
{
  "page_number": 1,
  "content": "AGE THE\nDATA SCIENCE\nINTERVIEW\n201 Real Interview Questions..."
}
```

**Output:**
```json
{
  "id": "ace_data_page_1",
  "date": "2025-11-21",
  "page_number": 1,
  "text": "AGE THE\nDATA SCIENCE\nINTERVIEW\n201 Real Interview Questions...",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Usage

1. Install the required dependencies:
   ```bash
   pip install tiktoken
   ```

2. Run the processing script:
   ```bash
   python process_ace_data.py --input text_chunker/ace_the_data.json --output ace_data_chunks.json
   ```
