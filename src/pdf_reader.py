import fitz  # PyMuPDF


def read_pdf_pages(
    pdf_path: str,
    start_page: int,
    end_page: int,
) -> str:
    """
    Reads text from a PDF between start_page and end_page (inclusive).

    Pages are 1-indexed to match human page numbering.
    PyMuPDF uses 0-indexed pages internally.
    """

    text_chunks = []

    with fitz.open(pdf_path) as doc:
        total_pages = len(doc)

        # Convert to 0-based index safely
        start_idx = max(start_page - 1, 0)
        end_idx = min(end_page, total_pages)

        for page_number in range(start_idx, end_idx):
            page = doc[page_number]
            page_text = page.get_text("text")
            text_chunks.append(page_text)

    return "\n".join(text_chunks)
