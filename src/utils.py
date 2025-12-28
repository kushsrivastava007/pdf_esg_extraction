# src/utils.py

import re


def extract_number(text: str):
    if not text:
        return None

    match = re.search(r"([\d,]+(?:\.\d+)?)", text)
    if match:
        return float(match.group(1).replace(",", ""))
    return None
