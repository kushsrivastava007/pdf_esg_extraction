
from typing import Dict, Any

from src.pdf_reader import read_pdf_pages


def _docling_extract(pdf_path: str) -> Dict[str, Any]:
    """Use Docling when available and configured correctly.

    This function imports Docling lazily so importing this module does not
    trigger heavy dependency initialisation at import time.
    """
    try:
        from docling.document_converter import DocumentConverter
    except Exception as e:
        raise ImportError(
            "Docling import failed. Activate your virtualenv and install docling.\n"
            "Example (PowerShell):\n  python -m venv .venv\n  .venv\\Scripts\\Activate.ps1\n"
            "Then: pip install docling\n"
            f"Original error: {e}"
        ) from e

    converter = DocumentConverter()
    doc = converter.convert(pdf_path)

    tables = []
    sections = []

    for item in doc.document_items:
        if item.type == "table":
            tables.append({
                "page": item.provenance.page_no,
                "rows": item.export_to_dataframe().to_dict(orient="records"),
            })
        elif item.type == "section":
            sections.append({"page": item.provenance.page_no, "title": item.text})

    return {"tables": tables, "sections": sections}


def extract_structured_content(pdf_path: str) -> Dict[str, Any]:
    """Try using Docling; on fatal errors provide guidance or fall back.

    - If Docling is missing, raise ImportError with installation hint so the
      caller can activate the venv and install it.
    - If Docling runs but conversion fails (e.g. missing models), fall back
      to a simple per-page text reader to keep the pipeline running.
    """
    try:
        return _docling_extract(pdf_path)
    except ImportError:
        # Surface the error so the user can install Docling in the venv.
        raise
    except Exception:
        # Fallback: return each page as one "row" with key 'text'.
        tables = []
        page_index = 1
        while True:
            try:
                page_text = read_pdf_pages(pdf_path, page_index, page_index)
            except Exception:
                break

            if not page_text.strip():
                break

            tables.append({"page": page_index, "rows": [{"text": page_text}]})
            page_index += 1

        return {"tables": tables, "sections": []}
