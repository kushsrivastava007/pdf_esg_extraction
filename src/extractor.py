from typing import List, Dict, Any
from collections import defaultdict

from src.pdf_reader import read_pdf_pages
from src.llm_agent import LLMExtractionAgent
from src.storage import ExtractionStore
from config.indicators import INDICATORS
from config.pages import PAGE_MAPPING


def run_extraction(
    companies: List[str],
    db_path: str,
) -> None:
    """
    Runs ESG extraction pipeline with CATEGORY-BASED batching.
    """

    agent = LLMExtractionAgent()
    store = ExtractionStore(db_path)

    for company in companies:
        print(f"\n=== Processing company: {company} ===")

        company_pages = PAGE_MAPPING.get(company)
        if not company_pages:
            print(f"⚠ No page references found for {company}, skipping.")
            continue

        # 1️⃣ Group indicators by category
        indicators_by_category: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        for indicator in INDICATORS:
            indicators_by_category[indicator["category"]].append(indicator)

        # 2️⃣ Process each category separately
        for category, indicators in indicators_by_category.items():
            print(f"\n📂 Category: {category}")

            combined_text_parts = []

            for indicator in indicators:
                page_range = company_pages.get(indicator["name"])
                if not page_range:
                    continue

                start_page, end_page = page_range
                print(
                    f"  → Reading pages {start_page}-{end_page} "
                    f"for indicator: {indicator['name']}"
                )

                text = read_pdf_pages(
                    pdf_path=company_pages["__pdf_path__"],
                    start_page=start_page,
                    end_page=end_page,
                )
                combined_text_parts.append(text)

            if not combined_text_parts:
                print("  ⚠ No text found for this category, skipping.")
                continue

            combined_text = "\n".join(combined_text_parts)

            print("🚀 Calling LLM (batch extraction)...")
            batch_results = agent.extract_many(
                indicators=indicators,
                text=combined_text,
            )

            # 3️⃣ Persist results
            for indicator in indicators:
                name = indicator["name"]
                result = batch_results.get(name)

                if not result:
                    store.insert(
                        company=company,
                        indicator_name=name,
                        category=indicator["category"],
                        esrs=indicator["esrs"],
                        value=None,
                        unit=indicator["expected_unit"],
                        confidence=0.0,
                        source_page=None,
                        source_section=None,
                        notes="Not found in batch extraction",
                    )
                    continue

                store.insert(
                    company=company,
                    indicator_name=name,
                    category=indicator["category"],
                    esrs=indicator["esrs"],
                    value=result.get("value"),
                    unit=result.get("unit"),
                    confidence=result.get("confidence", 0.0),
                    source_page=result.get("source_page"),
                    source_section=None,
                    notes=result.get("notes"),
                )

    print("\n✅ Extraction completed (category-batch mode).")
