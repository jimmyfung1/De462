import streamlit as st
import requests

def get_ollama_response(prompt, model="llama2"):
    """Call Ollama API - This function is provided"""
    url = "http://localhost:11434/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    try:
        response = requests.post(url, json=payload)
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"

# TODO: Add title and caption
st.___("🤖 My First AI Chatbot")
st.___("Powered by Ollama")

# TODO: Initialize 'chat_history' in session state
if "___" not in st.session_state:
    st.session_state.___ = ___

# TODO: Display all messages from chat history
for message in st.session_state.___:
    with st.chat_message(___["___"]):
        st.write(___["___"])

# TODO: Get user input
user_input = st.___("Ask me anything...")

if user_input:
    # TODO: Add user message to chat history
    st.session_state.___.append({"___": "user", "___": user_input})
    
    # TODO: Display user message
    with st.chat_message("___"):
        st.write(___)
    
    # TODO: Get AI response
    with st.chat_message("___"):
        with st.spinner("Thinking..."):
            ai_response = ___(user_input)
        st.write(___)
    
    # TODO: Add AI response to chat history
    st.session_state.___.append({"role": "___", "content": ___})