import json
import tiktoken
import argparse


def chunk_text(text, tokenizer, min_tokens=500, max_tokens=1000, overlap=100):
    tokens = tokenizer.encode(text)
    chunks = []
    start = 0
    text_len = len(tokens)

    while start < text_len:
        end = start + max_tokens
        if end > text_len:
            end = text_len
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)
        start += max_tokens - overlap

    return chunks


def process_file(input_path, output_path):
    encoding = tiktoken.get_encoding("cl100k_base")

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    chunked_data = []

    for item in data:
        text = item.get('text', '')
        chunks = chunk_text(text, encoding)
        for i, chunk in enumerate(chunks):
            chunked_item = item.copy()
            chunked_item['text'] = chunk
            chunked_item['chunk_index'] = i
            chunked_data.append(chunked_item)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunked_data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chunk large text documents into smaller pieces for embedding and vector search.')
    parser.add_argument('input', type=str, help='Input JSON file path')
    parser.add_argument('output', type=str, help='Output JSON file path')
    args = parser.parse_args()

    process_file(args.input, args.output)
