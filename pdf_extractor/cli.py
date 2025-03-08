"""
Command-line interface for PDF text extraction.
"""

import argparse
import os
import sys
import time

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
		help="Extraction method to use (use 'all' to run all methods)"
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
		method = ExtractionMethod(args.method.lower() if args.method.lower() == 'all' else args.method)
		
		# Initialize extractor
		extractor = PDFTextExtractor(args.file)
		
		if method == ExtractionMethod.ALL:
			# Run all methods and collect results
			print("Running all extraction methods...")
			results = {}
			
			for processing_method in ExtractionMethod.get_processing_methods():
				try:
					print(f"\nExtracting text using {processing_method.value}...")
					
					# Time the extraction process
					start_time = time.time()
					extracted_text = extractor.extract_text(processing_method)
					end_time = time.time()
					execution_time = end_time - start_time
					
					output_path = save_extracted_text(extracted_text, args.file, processing_method)
					
					results[processing_method.value] = {
						'text': extracted_text,
						'output_path': output_path,
						'stats': {
							'characters': len(extracted_text),
							'words': len(extracted_text.split()),
							'lines': len(extracted_text.splitlines()),
							'time': execution_time
						}
					}
					
					print(f"✓ Saved to: {output_path}")
					print(f"  Time taken: {execution_time:.2f} seconds")
					
				except Exception as e:
					print(f"✗ Failed: {str(e)}")
					results[processing_method.value] = {'error': str(e)}
			
			# Print comparative results in markdown format
			print("\n### Extraction Results Summary")
			print("\n| Method | Characters | Words | Lines | Time (seconds) |")
			print("|---------|------------|-------|-------|----------------|")
			
			for method_name, result in results.items():
				if 'stats' in result:
					stats = result['stats']
					print(f"| {method_name} | {stats['characters']:,} | {stats['words']:,} | "
						  f"{stats['lines']:,} | {stats['time']:.2f} |")
				else:
					print(f"| {method_name} | Failed: {result['error']} | - | - | - |")
			
			# Add a blank line at the end for better markdown formatting
			print()
			
		else:
			# Run single method with timing
			print(f"Extracting text using {method.value}...")
			
			start_time = time.time()
			extracted_text = extractor.extract_text(method)
			end_time = time.time()
			execution_time = end_time - start_time
			
			output_path = save_extracted_text(extracted_text, args.file, method)
			
			print(f"\nExtraction complete. File saved:")
			print(f"- {output_path}")
			print(f"Time taken: {execution_time:.2f} seconds")
			
			print_extraction_stats(method.value, extracted_text)
		
	except Exception as e:
		print(f"Error: {str(e)}", file=sys.stderr)
		sys.exit(1)
		
if __name__ == "__main__":
	main()