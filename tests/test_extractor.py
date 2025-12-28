from unittest.mock import patch

from src.extractor import run_extraction
from src.storage import ExtractionStore


def test_extractor_batch_mode(tmp_path):
    companies = [
        {"name": "TEST_CO", "pdf_path": "fake.pdf"}
    ]

    fake_indicators = [
        {
            "name": "Indicator A",
            "expected_unit": "units",
            "category": "Test",
            "esrs": "T1",
        },
        {
            "name": "Indicator B",
            "expected_unit": "units",
            "category": "Test",
            "esrs": "T2",
        },
    ]

    fake_pages = {
        "TEST_CO": {
            "Indicator A": (1, 2),
            "Indicator B": (3, 4),
        }
    }

    fake_llm_result = {
        "Indicator A": {
            "value": 10,
            "unit": "units",
            "confidence": 0.8,
            "source_page": 1,
            "notes": "Mocked",
        }
    }

    db_path = tmp_path / "test.sqlite"

    with patch("src.extractor.INDICATORS", fake_indicators), \
         patch("src.extractor.PAGE_REFERENCES", fake_pages), \
         patch("src.extractor.extract_text", return_value="fake text"), \
         patch("src.extractor.LLMExtractionAgent.extract_many", return_value=fake_llm_result):

        run_extraction(
            companies=companies,
            db_path=str(db_path),
        )

    store = ExtractionStore(db_path=str(db_path))
    rows = store.fetch_all_as_dicts()

    assert len(rows) == 2

    names = {r["indicator_name"] for r in rows}
    assert names == {"Indicator A", "Indicator B"}
