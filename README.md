# A simple package to extract text from PDFs

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