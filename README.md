To use the package:

As a command-line tool:

```bash
pdf-extract --method PDFPlumber --file path/to/document.pdf
```
As a library in another project:

```python
from pdf_extractor import PDFTextExtractor, ExtractionMethod

extractor = PDFTextExtractor("path/to/document.pdf")
text = extractor.extract_text(ExtractionMethod.PDFPLUMBER)
```