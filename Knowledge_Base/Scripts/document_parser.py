from pathlib import Path

from docling.document_converter import DocumentConverter


def load_document(pdf_path: Path):

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    converter = DocumentConverter()

    result = converter.convert(pdf_path)

    return result.document

