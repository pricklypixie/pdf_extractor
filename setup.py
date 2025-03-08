from setuptools import setup, find_packages

setup(
	name="pdf_extractor",
	version="0.1.0",
	packages=find_packages(),
	install_requires=[
		"pdfplumber",
		"PyPDF2",
		"PyMuPDF",
		"transformers",
		"torch",
		"Pillow",
	],
	entry_points={
		'console_scripts': [
			'pdf-extract=pdf_extractor.cli:main',
		],
	},
)