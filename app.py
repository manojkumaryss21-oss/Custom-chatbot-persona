import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
st.set_page_config(page_title="Custom Chatbot Persona", page_icon="🤖", layout="wide")

st.title("🤖 Custom Chatbot Persona")
st.caption("Project A | Build a chatbot whose behaviour is controlled by a system prompt.")

PERSONAS = {
    "Teacher Bot": "You are a patient college teacher. Explain topics in simple English, use headings and examples, and keep explanations suitable for students.",
    "Career Guide": "You are a supportive career guide. Give practical, balanced advice about skills, learning paths, and career preparation. Do not guarantee outcomes.",
    "Technical Assistant": "You are a technical assistant. Explain programming and technology clearly, use small examples, and state assumptions when needed.",
    "Friendly Assistant": "You are a friendly, respectful general assistant. Be clear, concise, and helpful."
}

def get_api_key():
    try:
        return st.secrets.get("OPENAI_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")
    except Exception:
        return os.getenv("OPENAI_API_KEY", "")

def get_ai_reply(prompt, history, question):
    key = get_api_key()
    if not key:
        # Offline demo response so the UI can be demonstrated without an API key.
        return (
            "**Demo mode (no API key configured)**\n\n"
            f"Your selected system prompt begins: _{prompt[:180]}..._\n\n"
            f"You asked: **{question}**\n\n"
            "This demonstration shows how the chatbot interface receives a question and "
            "applies a persona. Add an OpenAI API key in your environment or Streamlit "
            "secrets to receive live AI-generated answers."
        )
    client = OpenAI(api_key=key)
    transcript = []
    for item in history[-10:]:
        transcript.append(f'{item["role"].upper()}: {item["content"]}')
    transcript.append(f"USER: {question}")
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
        instructions=prompt,
        input="\n\n".join(transcript),
    )
    return response.output_text

with st.sidebar:
    st.header("Chatbot settings")
    persona = st.selectbox("Choose a persona", list(PERSONAS) + ["Custom"])
    default_prompt = PERSONAS.get(persona, "You are a helpful assistant. Answer accurately, clearly, and politely.")
    system_prompt = st.text_area("System prompt", value=default_prompt, height=220)
    st.caption("The system prompt defines the chatbot's role, tone, and response rules.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader(f"Chat with {persona}")
st.write("Try asking a question and then change the persona or system prompt to compare the responses.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Type your question here...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("Preparing response..."):
            try:
                answer = get_ai_reply(system_prompt, st.session_state.messages[:-1], question)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as error:
                st.error(f"Could not generate a response: {error}")

with st.expander("Project explanation"):
    st.markdown("""
    **Aim:** To develop a customizable chatbot using system prompts.

    **Working:** The user selects a persona or writes a custom system prompt. The prompt is sent as the model's instructions, and the chatbot responds according to those instructions.

    **Experiment:** Ask the same question using Teacher Bot and Technical Assistant. Compare tone, structure, and level of detail.
    """)
