"""
Command-line interface for PDF text extraction.
"""

import argparse
import os
import sys
from .extractor import PDFTextExtractor, ExtractionMethod

def save_extracted_text(text: str, pdf_path: str, method: ExtractionMethod) -> str:
	"""
	Save extracted text to a file.
	
	Args:
		text (str): The extracted text to save
		pdf_path (str): Path to the original PDF file
		method (ExtractionMethod): The extraction method used
		
	Returns:
		str: Path to the saved file
	"""
	dir_path = os.path.dirname(pdf_path)
	base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
	
	# Create method-specific filename
	method_suffix = method.value.lower()
	if method == ExtractionMethod.DONUT:
		method_suffix = "donut-base-finetuned-docvqa"
	elif method == ExtractionMethod.LAYOUTLM:
		method_suffix = "layoutlm-base-uncased"
	
	output_path = os.path.join(dir_path, f"{base_filename}-{method_suffix}.txt")
	
	with open(output_path, "w", encoding="utf-8") as f:
		f.write(text)
	
	return output_path

def print_extraction_stats(method_name: str, text: str):
	"""Print basic statistics about the extracted text."""
	num_chars = len(text)
	num_words = len(text.split())
	num_lines = len(text.splitlines())
	print(f"\n{method_name} Statistics:")
	print(f"- Characters: {num_chars:,}")
	print(f"- Words: {num_words:,}")
	print(f"- Lines: {num_lines:,}")

def main():
	"""Main function with argument parsing."""
	parser = argparse.ArgumentParser(description="Extract text from PDF documents using various methods.")
	
	parser.add_argument(
		"--method",
		type=str,
		choices=[method.value for method in ExtractionMethod],
		required=True,
		help="Extraction method to use"
	)
	
	parser.add_argument(
		"--file",
		type=str,
		required=True,
		help="Path to the PDF file"
	)
	
	args = parser.parse_args()
	
	try:
		# Convert method string to enum
		method = ExtractionMethod(args.method)
		
		# Initialize extractor and process file
		extractor = PDFTextExtractor(args.file)
		print(f"Extracting text using {method.value}...")
		
		# Extract and save text
		extracted_text = extractor.extract_text(method)
		output_path = save_extracted_text(extracted_text, args.file, method)
		
		# Print results
		print(f"\nExtraction complete. File saved:")
		print(f"- {output_path}")
		
		# Print statistics
		print_extraction_stats(method.value, extracted_text)
		
	except Exception as e:
		print(f"Error: {str(e)}", file=sys.stderr)
		sys.exit(1)

if __name__ == "__main__":
	main()