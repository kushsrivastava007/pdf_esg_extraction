from src.llm_agent import LLMExtractionAgent
from src.ollama import OllamaLLM


def test_extract_many_parses_json(monkeypatch):
    fake_response = """
    {
      "Scope 1 GHG Emissions": {
        "value": 245000,
        "unit": "tCO2e",
        "confidence": 0.9,
        "source_page": 120,
        "notes": "From emissions table"
      }
    }
    """

    def fake_invoke(self, prompt):
        return fake_response  # ✅ return STRING

    monkeypatch.setattr(OllamaLLM, "invoke", fake_invoke)

    agent = LLMExtractionAgent()

    indicators = [
        {
            "name": "Scope 1 GHG Emissions",
            "definition": "Direct emissions",
            "expected_unit": "tCO2e",
        }
    ]

    result = agent.extract_many(indicators, "fake text")

    assert "Scope 1 GHG Emissions" in result
    assert result["Scope 1 GHG Emissions"]["value"] == 245000
