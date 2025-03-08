"""
PDF Text Extractor package.
Provides multiple methods for extracting text from PDF documents.
"""

from .extractor import PDFTextExtractor, ExtractionMethod

__version__ = "0.1.0"
__all__ = ['PDFTextExtractor', 'ExtractionMethod']