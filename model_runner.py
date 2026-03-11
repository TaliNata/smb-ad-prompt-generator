import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


MODELS = [
    "openai/gpt-4o-mini",
    "anthropic/claude-3-haiku",
    "meta-llama/llama-3.1-70b-instruct",
]


def call_model(model, prompt):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={"model": model, "messages": [{"role": "user", "content": prompt}]},
    )

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except Exception:
        return f"Error from model {model}: {data}"


def run_model_comparison(prompt):

    for model in MODELS:

        print(f"\n--- MODEL: {model} ---\n")

        result = call_model(model, prompt)

        print(result)

        print("\n----------------------------------------\n")
