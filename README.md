# A simple package to extract text from PDFs

## Install

```bash
pip install git+https://github.com/pricklypixie/pdf-extractor.git
```

## To use the package:

### As a command-line tool:

```bash
pdf-extract --method PDFPlumber --file path/to/document.pdf
(uses pdfplumber - [https://github.com/jsvine/pdfplumber](https://github.com/jsvine/pdfplumber))

pdf-extract --method PyMuPDF --file path/to/document.pdf
(uses PyMuPDF - [https://pymupdf.io](https://pymupdf.io))

pdf-extract --method PyPDF2 --file path/to/document.pdf
(uses PyMuPDF - [https://github.com/py-pdf/pypdf/](https://github.com/py-pdf/pypdf/))


pdf-extract --method Donut --file path/to/document.pdf
(uses Donut - [https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa](https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa))

pdf-extract --method LayoutLM --file path/to/document.pdf
(uses LayoutLM - [https://huggingface.co/microsoft/layoutlm-base-uncased](https://huggingface.co/microsoft/layoutlm-base-uncased))
```
### As a library in another project:

```python
from pdf_extractor import PDFTextExtractor, ExtractionMethod

extractor = PDFTextExtractor("path/to/document.pdf")
text = extractor.extract_text(ExtractionMethod.PDFPLUMBER)
```