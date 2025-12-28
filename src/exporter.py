"""
CSV exporter for extraction results.

Responsibility:
- Read all rows from SQLite
- Write them into a CSV file

No LLM, no PDF logic here.
"""

import csv
from pathlib import Path
from typing import List, Dict, Any

from src.storage import ExtractionStore


def export_to_csv(
    db_path: str,
    output_csv_path: str,
):
    """
    Export extraction results from SQLite to CSV.

    Args:
        db_path: Path to SQLite database
        output_csv_path: Path where CSV should be written
    """

    store = ExtractionStore(db_path=db_path)
    rows: List[Dict[str, Any]] = store.fetch_all_as_dicts()

    if not rows:
        print("⚠ No data found in database. CSV not created.")
        return

    output_path = Path(output_csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=rows[0].keys(),
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ CSV exported successfully: {output_path}")
