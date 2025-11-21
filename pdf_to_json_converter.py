import json
import PyPDF2
from typing import Dict, List, Any

def extract_text_from_pdf(pdf_path: str) -> List[Dict[str, Any]]:
    """
    Extract text from each page of a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        List of dictionaries containing page number and extracted text
    """
    pages_data = []
    
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                
                pages_data.append({
                    'page_number': page_num + 1,
                    'content': text.strip()
                })
                
    except Exception as e:
        print(f"Error processing PDF: {e}")
        raise
    
    return pages_data

def save_to_json(data: List[Dict[str, Any]], output_path: str) -> None:
    """
    Save extracted data to a JSON file.
    
    Args:
        data: Data to be saved
        output_path: Path where the JSON file will be saved
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        print(f"Successfully saved extracted data to {output_path}")
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        raise

def convert_pdf_to_json(pdf_path: str, json_path: str) -> None:
    """
    Convert a PDF file to JSON format.
    
    Args:
        pdf_path: Path to the input PDF file
        json_path: Path where the output JSON file will be saved
    """
    print(f"Starting conversion of {pdf_path} to JSON...")
    pages_data = extract_text_from_pdf(pdf_path)
    save_to_json(pages_data, json_path)

if __name__ == "__main__":
    # Example usage
    input_pdf = "/Users/abiodungbadamosi/CascadeProjects/windsurf-project/ace_the_data.pdf"  # Replace with your PDF path
    output_json = "ace_the_data.json"  # Output JSON file name
    
    convert_pdf_to_json(input_pdf, output_json)
