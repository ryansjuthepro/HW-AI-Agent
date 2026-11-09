import os

from google import genai
from google.genai import types


def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Set the GEMINI_API_KEY environment variable before running.")

    with genai.Client(api_key=api_key) as client:
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents="Hello! Explain what an AI agent is in one sentence.",
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful assistant. Keep answers concise.",
            ),
        )
        print(response.text)


if __name__ == "__main__":
    main()
