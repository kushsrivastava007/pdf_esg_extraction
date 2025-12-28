import json
import re
from typing import List, Dict, Any

from src.ollama import OllamaLLM


class LLMExtractionAgent:
    """
    Batch extraction agent using a local Ollama LLM (Mistral).
    """

    def __init__(self):
        self.model = OllamaLLM(model="qwen2.5:7b")

    def extract_many(
        self,
        indicators: List[Dict[str, Any]],
        text: str,
    ) -> Dict[str, Dict[str, Any]]:
        """
        Extracts all indicators in ONE batch LLM call.

        Returns:
            Dict[indicator_name -> extracted_fields]
            Empty dict if parsing fails.
        """

        indicator_block = "\n".join(
            f"- {i['name']} ({i['expected_unit']}): {i['definition']}"
            for i in indicators
        )

        prompt = f"""
You are an information extraction system.

Extract the following ESG indicators from the text.

Rules:
- Return ONLY valid JSON
- Keys must match indicator names EXACTLY
- If an indicator is not found, return null
- Do NOT infer or guess
- Do NOT add commentary or explanations

Indicators:
{indicator_block}

Text:
{text}

Return JSON in the following format:
{{
  "Indicator Name": {{
    "value": number or null,
    "unit": string,
    "confidence": number between 0 and 1,
    "source_page": number or null,
    "notes": string
  }}
}}
"""

        raw = self.model.invoke(prompt)

        return self._safe_parse_json(raw)

    @staticmethod
    def _safe_parse_json(raw: str) -> Dict[str, Any]:
        """
        Safely extracts and parses JSON from LLM output.

        - Removes markdown fences
        - Extracts first JSON object
        - Returns empty dict on failure (NO crash)
        """

        if not raw:
            return {}

        # Remove markdown fences if present
        cleaned = raw.replace("```json", "").replace("```", "").strip()

        # Extract first JSON object using regex
        match = re.search(r"\{.*\}", cleaned, re.DOTALL)

        if not match:
            return {}

        json_text = match.group(0)

        try:
            parsed = json.loads(json_text)
            return parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            return {}
