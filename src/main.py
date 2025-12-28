from pathlib import Path

from src.extractor import run_extraction
from src.exporter import export_to_csv


def main() -> None:
    # Companies are IDENTIFIERS (strings), not dicts
    companies = ["AIB", "BPCE", "BBVA"]

    # Paths
    base_dir = Path(__file__).resolve().parent.parent
    db_path = base_dir / "db" / "extractions.sqlite"
    output_csv = base_dir / "output" / "extractions.csv"

    # Ensure folders exist
    db_path.parent.mkdir(exist_ok=True)
    output_csv.parent.mkdir(exist_ok=True)

    # Run extraction
    run_extraction(
        companies=companies,
        db_path=str(db_path),
    )

    # Export to CSV
    export_to_csv(
        db_path=str(db_path),
        output_csv_path=str(output_csv),
    )


if __name__ == "__main__":
    main()
