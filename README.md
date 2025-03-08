# A simple package to extract text from PDFs

We often have to compare packages that could be used to perform the same task. 

Lots of document processing tasks require text to be extracted from PDFs. 

This package is intended to help test different text extraction packages to help choose the best for the type of source documents being incorporated into other projects.

## Install

```bash
pip install git+https://github.com/pricklypixie/pdf-extractor.git
```

## To use the package:

### As a command-line tool:

```bash
# using pdfplumber
pdf-extract --method PDFPlumber --file path/to/document.pdf

# using PyMuPDF
pdf-extract --method PyMuPDF --file path/to/document.pdf

# using PyMuPDF
pdf-extract --method PyPDF2 --file path/to/document.pdf

# using Donut
pdf-extract --method Donut --file path/to/document.pdf

# using LayoutLM
pdf-extract --method LayoutLM --file path/to/document.pdf
```

To test and compare all available text extraction packages:

```bash
pdf-extract --method all --file path/to/document.pdf
```

A file will be save in the same directory as the source document in the format: document-package.txt

### As a library in another project:

```python
from pdf_extractor import PDFTextExtractor, ExtractionMethod

extractor = PDFTextExtractor("path/to/document.pdf")
text = extractor.extract_text(ExtractionMethod.PDFPLUMBER)
```


## Source PDF extraction libraries

pdfplumber - [https://github.com/jsvine/pdfplumber](https://github.com/jsvine/pdfplumber)

PyMuPDF - [https://pymupdf.io](https://pymupdf.io)

PyMuPDF - [https://github.com/py-pdf/pypdf/](https://github.com/py-pdf/pypdf/)

Donut - [https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa](https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa)

LayoutLM - [https://huggingface.co/microsoft/layoutlm-base-uncased](https://huggingface.co/microsoft/layoutlm-base-uncased)