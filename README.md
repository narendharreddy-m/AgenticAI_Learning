# AgenticAI_Learning – API Integration (Groq + Python)
This project demonstrates how to build a simple Python-based AI client using the Groq API to generate responses from an LLM.

# Overview
Uses Python with requests
Loads API keys securely using .env
Sends prompts to an LLM (llama3-8b-8192)
Prints model responses in the terminal

# Setup Instructions
1. Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
2. Add environment variables
Create a .env file:
```
GROQ_API_KEY=your_api_key_here
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Application
```
python3 api.py
```

# Troubleshooting
1. ModuleNotFoundError
```
pip install requests python-dotenv
```
2. 401 Unauthorized
```
**Check API key**

**Ensure correct endpoint:**

https://api.groq.com/openai/v1/chat/completions
```
3. dotenv not found in VS Code
```
Select correct interpreter (venv/bin/python)
```
4. SSL Warning (LibreSSL)
```
Recreate virtual environment using Homebrew Python
```