import sqlite3
from typing import Optional, List, Dict, Any


class ExtractionStore:
    """
    SQLite-backed storage for ESG indicator extractions.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS extractions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT NOT NULL,
                    indicator_name TEXT NOT NULL,
                    category TEXT,
                    esrs TEXT,
                    value TEXT,
                    unit TEXT,
                    confidence REAL,
                    source_page INTEGER,
                    source_section TEXT,
                    notes TEXT
                )
                """
            )
            conn.commit()

    # ------------------------
    # WRITE API
    # ------------------------
    def insert(
        self,
        company: str,
        indicator_name: str,
        category: Optional[str],
        esrs: Optional[str],
        value: Optional[str],
        unit: Optional[str],
        confidence: float,
        source_page: Optional[int],
        source_section: Optional[str],
        notes: Optional[str],
    ) -> None:
        """
        Inserts exactly one extraction row.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO extractions (
                    company,
                    indicator_name,
                    category,
                    esrs,
                    value,
                    unit,
                    confidence,
                    source_page,
                    source_section,
                    notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    company,
                    indicator_name,
                    category,
                    esrs,
                    value,
                    unit,
                    confidence,
                    source_page,
                    source_section,
                    notes,
                ),
            )
            conn.commit()

    # ------------------------
    # READ API (THIS FIXES YOUR ERROR)
    # ------------------------
    def fetch_all_as_dicts(self) -> List[Dict[str, Any]]:
        """
        Fetches all extraction rows as a list of dictionaries.
        Used by exporter.py.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM extractions")
            rows = cursor.fetchall()

            return [dict(row) for row in rows]
