import requests

# Replace this with your actual key
OPENROUTER_API_KEY = "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"

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",  # required but can be anything
        "X-Title": "SpecGPT-Dev"
    },
    json={
        "model": "openai/gpt-3.5-turbo",  # Or try "openai/gpt-4" or "anthropic/claude-3-opus-20240229"
        "messages": [
            {"role": "user", "content": "Hello, world!"}
        ]
    }
)

result = response.json()
print("\n🤖 Response:", result["choices"][0]["message"]["content"])
