import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiService:

    @staticmethod
    def generate_qa(content: str):

        prompt = f"""
You are a QA engineer.

Generate 5 question-answer pairs from the following document.

Return ONLY valid JSON in this format:

[
    {{
        "question": "...",
        "answer": "..."
    }}
]

Document:

{content}
"""

        response = client.models.generate_content(
            model="models/gemini-3.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)