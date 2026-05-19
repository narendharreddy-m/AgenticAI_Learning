import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

body = {
    "model": "openai/gpt-oss-120b",   # Groq-supported model
    "messages": [
        {"role": "system", "content": "You are a helpful Python tutor. Keep replies under 3 sentences."},
        {"role": "user", "content": "What is an API key in one line?"},
    ],
}
response = requests.post(url, headers=headers, json=body, timeout=30)

print("Status Code:", response.status_code)
print("Response:", response.text)