from src.pdf_reader import extract_text, extract_text_single_page
from pathlib import Path

pdf_path = Path("data") / "aib-group-plc-afr-report-2024.pdf"


def test_extract_text_range():
    

    text = extract_text(
        pdf_path=str(pdf_path),
        start_page=1,
        end_page=2
    )

    assert isinstance(text, str)
    assert len(text.strip()) > 0


def test_extract_single_page():
   
    text = extract_text_single_page(
        pdf_path=str(pdf_path),
        page_number=1
    )

    assert isinstance(text, str)
    assert len(text.strip()) > 0
