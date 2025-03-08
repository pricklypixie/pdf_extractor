# A simple package to extract text from PDFs

We often have to compare packages that could be used to perform the same task. 

Lots of document processing tasks require text to be extracted from PDFs. 

This package is intended to help test different text extraction packages to help choose the best for the type of source documents being incorporated into other projects.

## Install

To install from Github:

```bash
pip install git+https://github.com/pricklypixie/pdf-extractor.git
```

To install from downloaded package:

```bash
git clone https://github.com/pricklypixie/pdf-extractor.git
cd pdf-extractor
pip install -e .
```

## Use the package as a command-line tool:

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

### Sample output

```bash
pdf-extract --method all --file path/to/document.pdf
```


=== Extraction Results Summary ===

| Method | Characters | Words | Lines | Time (seconds) |
|---------|------------|-------|-------|----------------|
| PDFPlumber | 51,529 | 2,858 | 785 | 3.99 |
| PyMuPDF | 56,988 | 8,291 | 1,515 | 0.14 |
| PyPDF2 | 56,929 | 8,255 | 738 | 1.96 |
| Donut | 458 | 60 | 22 | 29.82 |
| LayoutLM | 851 | 131 | 23 | 46.22 |



## Use the package as a library in another project:

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

## Use of AI/LLMs

Extensive use of [Anthropic Claude](https://www.anthropic.com) was used to create the code in this repository.

