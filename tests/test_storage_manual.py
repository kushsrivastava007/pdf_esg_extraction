import os
from src.storage import ExtractionStore


def test_insert_and_fetch_storage(tmp_path):
    """
    Test that a row can be inserted into SQLite
    and fetched back correctly.
    """

    # Use pytest-provided temporary directory
    db_path = tmp_path / "test_extractions.sqlite"

    store = ExtractionStore(db_path=str(db_path))

    indicator = {
        "name": "Test Indicator",
        "category": "Environmental",
        "esrs": "E1",
    }

    result = {
        "value": 123,
        "unit": "tCO2e",
        "confidence": 0.9,
        "source_page": 5,
        "source_section": "Test Section",
        "notes": "Pytest storage test",
    }

    store.insert_result(
        company="TEST_COMPANY",
        indicator=indicator,
        result=result,
    )

    rows = store.fetch_all_as_dicts()

    assert len(rows) == 1

    row = rows[0]

    assert row["company"] == "TEST_COMPANY"
    assert row["indicator_name"] == "Test Indicator"
    assert row["value"] == "123"   # stored as TEXT
    assert row["unit"] == "tCO2e"
    assert row["confidence"] == 0.9
