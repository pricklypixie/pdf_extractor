"""
Core functionality for PDF text extraction.
Provides different methods for extracting text from PDF documents.

See the Readme for further information.

"""

import os
import tempfile
from enum import Enum
import pdfplumber
import PyPDF2
import fitz
from PIL import Image
from transformers import pipeline

class ExtractionMethod(Enum):
	"""Enumeration of available extraction methods."""
	PDFPLUMBER = "PDFPlumber"
	PYMUPDF = "PyMuPDF"
	PYPDF2 = "PyPDF2"
	DONUT = "Donut"
	LAYOUTLM = "LayoutLM"
	
	@classmethod
	def list_methods(cls):
		"""Return list of available method names."""
		return [method.value for method in cls]

class PDFTextExtractor:
	"""
	A class that provides multiple methods for extracting text from PDF documents.
	"""

	def __init__(self, pdf_path):
		"""
		Initialize the extractor with a PDF file path.
		
		Args:
			pdf_path (str): Path to the PDF file
		"""
		self.pdf_path = pdf_path
		self._validate_file()

	def _validate_file(self):
		"""Validate that the PDF file exists and is accessible."""
		if not os.path.exists(self.pdf_path):
			raise FileNotFoundError(f"PDF file not found: {self.pdf_path}")
		if not self.pdf_path.lower().endswith('.pdf'):
			raise ValueError("File must be a PDF document")

	def extract_text(self, method: ExtractionMethod) -> str:
		"""
		Extract text using the specified method.
		
		Args:
			method (ExtractionMethod): The extraction method to use
			
		Returns:
			str: Extracted text
		"""
		if method == ExtractionMethod.PDFPLUMBER:
			return self.extract_with_pdfplumber()
		elif method == ExtractionMethod.PYMUPDF:
			return self.extract_with_pymupdf()
		elif method == ExtractionMethod.PYPDF2:
			return self.extract_with_pypdf2()
		elif method == ExtractionMethod.DONUT:
			return self.extract_with_ai()
		elif method == ExtractionMethod.LAYOUTLM:
			return self.extract_with_ai_ms()
		else:
			raise ValueError(f"Unsupported extraction method: {method}")

	def extract_with_pdfplumber(self):
		"""Extract text using pdfplumber."""
		extracted_text = []
		with pdfplumber.open(self.pdf_path) as pdf:
			for page in pdf.pages:
				extracted_text.append(page.extract_text())
		return '\n'.join(extracted_text)

	def extract_with_pymupdf(self):
		"""Extract text using PyMuPDF (fitz)."""
		extracted_text = []
		with fitz.open(self.pdf_path) as doc:
			for page in doc:
				extracted_text.append(page.get_text())
		return '\n'.join(extracted_text)

	def extract_with_pypdf2(self):
		"""Extract text using PyPDF2."""
		extracted_text = []
		with open(self.pdf_path, 'rb') as file:
			reader = PyPDF2.PdfReader(file)
			for page in reader.pages:
				extracted_text.append(page.extract_text())
		return '\n'.join(extracted_text)

	def extract_with_ai(self):
		"""Extract text using Donut AI model."""
		import shutil
		
		try:
			processor = pipeline(
				"document-question-answering",
				model="naver-clova-ix/donut-base-finetuned-docvqa",
				device="mps",
				model_kwargs={"attn_implementation": "eager"}
			)
			
			temp_dir = tempfile.mkdtemp()
			try:
				doc = fitz.open(self.pdf_path)
				image_paths = []
				
				for page_num in range(len(doc)):
					page = doc[page_num]
					pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
					image_path = os.path.join(temp_dir, f"page_{page_num}.png")
					pix.save(image_path)
					image_paths.append(image_path)
				
				doc.close()
				
				extracted_text = []
				for image_path in image_paths:
					image = Image.open(image_path)
					
					try:
						result = processor(
							image=image,
							question="Extract all text from this document."
						)
						
						if isinstance(result, list):
							text = result[0]['answer'] if result else ""
						elif isinstance(result, dict):
							text = result.get('answer', '')
						else:
							text = str(result)
						
						if isinstance(text, dict):
							text = text.get('answer', text.get('text', str(text)))
						
						if text is not None and str(text).strip():
							extracted_text.append(str(text).strip())
						
					except Exception as e:
						print(f"Warning: Failed to process page {image_path}: {str(e)}")
						continue
				
				return '\n'.join(extracted_text) if extracted_text else "No text could be extracted"
				
			finally:
				shutil.rmtree(temp_dir)
				
		except Exception as e:
			raise Exception(f"AI extraction failed: {str(e)}")

	def extract_with_ai_ms(self):
		"""Extract text using LayoutLM AI model."""
		import shutil
		
		try:
			processor = pipeline(
				"document-question-answering",
				model="microsoft/layoutlm-base-uncased",
				device="mps",
				model_kwargs={"attn_implementation": "eager"}
			)
			
			temp_dir = tempfile.mkdtemp()
			try:
				doc = fitz.open(self.pdf_path)
				image_paths = []
				
				for page_num in range(len(doc)):
					page = doc[page_num]
					pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
					image_path = os.path.join(temp_dir, f"page_{page_num}.png")
					pix.save(image_path)
					image_paths.append(image_path)
				
				doc.close()
				
				extracted_text = []
				for image_path in image_paths:
					image = Image.open(image_path)
					
					try:
						result = processor(
							image=image,
							question="Extract all text from this document."
						)
						
						if isinstance(result, list):
							text = result[0]['answer'] if result else ""
						elif isinstance(result, dict):
							text = result.get('answer', '')
						else:
							text = str(result)
						
						if isinstance(text, dict):
							text = text.get('answer', text.get('text', str(text)))
						
						if text is not None and str(text).strip():
							extracted_text.append(str(text).strip())
						
					except Exception as e:
						print(f"Warning: Failed to process page {image_path}: {str(e)}")
						continue
				
				return '\n'.join(extracted_text) if extracted_text else "No text could be extracted"
				
			finally:
				shutil.rmtree(temp_dir)
				
		except Exception as e:
			raise Exception(f"AI extraction failed: {str(e)}")