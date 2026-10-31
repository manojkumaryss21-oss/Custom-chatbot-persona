# Project A – Custom Chatbot Persona with System Prompts

## Aim
Develop a chatbot whose role, tone, and response style are controlled by a system prompt.

## Features
- Four ready-made personas: Teacher, Career Guide, Technical Assistant, Friendly Assistant.
- Custom system prompt editor.
- Chat interface and conversation history.
- Clear conversation button.
- Demo mode works without an API key; live AI mode is enabled by configuring an OpenAI API key.

## Technology
Python 3.10+, Streamlit, OpenAI Python SDK.

## Run on a laptop

1. Install Python 3.10 or newer.
2. Extract this ZIP and open a terminal in the extracted folder.
3. Create a virtual environment (optional but recommended):
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Optional live AI: copy `.env.example` to `.env` and add your own API key. Never share or commit this file. Without a key, the app runs in demo mode.
6. Start: `streamlit run app.py`
7. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Run on Android
Deploy the project from GitHub using Streamlit Community Cloud, then open its app URL in Chrome. The app is responsive and does not require Python on Android.

## GitHub upload

Create a new GitHub repository named `custom-chatbot-persona`. Upload the contents of this folder (not the ZIP itself), then commit the files.

Alternatively, from a terminal:
```bash
git init
git add .
git commit -m "Add custom chatbot persona project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/custom-chatbot-persona.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username.

## Streamlit Community Cloud deployment
1. Sign in at https://share.streamlit.io/ using GitHub.
2. Choose **Create app** and select your repository.
3. Branch: `main`; main file: `app.py`.
4. Deploy. To enable live AI, add `OPENAI_API_KEY = "your-key"` in the app's Secrets settings. Keep the key private.
5. The app runs in demo mode if no key is configured.

## Test cases
1. Select Teacher Bot and ask: "Explain cloud computing."
2. Select Technical Assistant and ask the same question.
3. Select Custom and enter your own system prompt.
4. Clear the conversation and verify the chat resets.

## Result
A working web-based chatbot demonstrates how system prompts influence an AI assistant's behaviour.
