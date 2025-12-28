import requests


class OllamaLLM:
    """
    Minimal Ollama client for local LLM inference.
    """

    def __init__(
        self,
        model: str = "qwen2.5:7b",
        base_url: str = "http://localhost:11434",
    ):
        self.model = model
        self.url = f"{base_url}/api/generate"

    def invoke(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
                "num_predict": 800,  # limit output size
            },
        }

        response = requests.post(
            self.url,
            json=payload,
            timeout=900,  # 15 minutes
        )
        response.raise_for_status()

        return response.json()["response"]

