import streamlit as st
import requests
import json
from datetime import datetime

def get_available_models():
    """Get list of available Ollama models"""
    try:
        # TODO: Make GET request to Ollama tags endpoint
        response = requests.get("http://localhost:11434/api/___")
        response.raise_for_status()
        models = response.json()["___"]
        # TODO: Return list of model names
        return [model["___"] for model in models]
    except:
        return ["llama3.2:latest"]  # Fallback

def stream_with_options(messages, model="llama3.2:latest", temperature=0.7, system_prompt=None):
    """Stream with advanced options - Part 9 + customization!"""
    url = "http://localhost:11434/api/chat"
    
    # TODO: Add system prompt if provided
    full_messages = messages.copy()
    if system_prompt:
        # Insert system message at the beginning
        full_messages.insert(0, {"role": "___", "content": ___})
    
    # TODO: Create payload with temperature option
    payload = {
        "model": ___,
        "messages": ___,
        "stream": True,
        "options": {
            "___": ___  # Add temperature!
        }
    }
    
    try:
        response = requests.post(url, json=payload, stream=True)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                if "message" in chunk and "content" in chunk["message"]:
                    yield chunk["message"]["content"]
    
    except requests.exceptions.ConnectionError:
        yield "Error: Could not connect to Ollama. Make sure it's running!"
    except requests.exceptions.RequestException as e:
        yield f"Error: Request failed: {str(e)}"
    except Exception as e:
        yield f"Error: {str(e)}"

st.set_page_config(page_title="Advanced Chatbot", page_icon="🚀", layout="wide")

st.title("🚀 Advanced AI Chatbot")
st.caption("Building on Part 9 - Full control over AI behavior")

# TODO: Initialize messages
if "___" not in st.session_state:
    st.session_state.___ = []

# Sidebar - Settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # TODO: Get available models and create selector
    available_models = ___()
    selected_model = st.___(
        "Choose Model",
        ___,
        help="Select which Ollama model to use"
    )
    
    # TODO: Temperature slider
    temperature = st.___(
        "Temperature",
        min_value=___,
        max_value=___,
        value=0.7,
        step=0.1,
        help="Lower = focused, Higher = creative"
    )
    
    # TODO: System prompt text area
    st.subheader("System Prompt")
    system_prompt = st.___(
        "Set AI behavior",
        value="You are a helpful assistant.",
        height=100
    )
    
    # TODO: Preset buttons
    st.caption("Quick Presets:")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💼 Professional", use_container_width=True):
            system_prompt = "You are a professional assistant. Be formal and concise."
            st.rerun()
        
        if st.button("🎨 Creative", use_container_width=True):
            system_prompt = "You are a creative writer. Be imaginative and engaging."
            st.rerun()
    
    with col2:
        if st.button("👨‍💻 Programmer", use_container_width=True):
            system_prompt = "You are an expert programmer. Provide clear code examples."
            st.rerun()
        
        if st.button("🧑‍🏫 Teacher", use_container_width=True):
            system_prompt = "You are a patient teacher. Explain clearly with examples."
            st.rerun()
    
    st.divider()
    
    # TODO: Clear chat button
    st.subheader("Chat Controls")
    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.___ = []
        st.rerun()
    
    # TODO: Export chat button
    if st.button("💾 Export Chat", use_container_width=True):
        if st.session_state.___:
            # Create chat text
            chat_text = f"Chat Export - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            chat_text += f"Model: {___}\n"
            chat_text += f"Temperature: {___}\n\n"
            
            for msg in st.session_state.___:
                role = msg["___"].upper()
                chat_text += f"{role}: {msg['___']}\n\n"
            
            # TODO: Create download button
            st.___(
                "📥 Download",
                ___,
                file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
    
    st.divider()
    
    # TODO: Display stats
    st.subheader("📊 Stats")
    st.metric("Messages", len(st.session_state.___))
    st.metric("Model", ___)
    st.metric("Temperature", f"{___:.1f}")

# TODO: Display messages
for message in st.session_state.___:
    with st.chat_message(message["___"]):
        st.write(message["___"])

# TODO: Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # TODO: Add user message
    st.session_state.___.append({"role": "___", "content": ___})
    with st.chat_message("___"):
        st.write(___)
    
    # TODO: Get AI response with all options
    with st.chat_message("assistant"):
        message_placeholder = st.___()
        full_response = ""
        
        # Stream with all advanced options
        for chunk in ___(
            st.session_state.___,
            model=___,  # User-selected model
            temperature=___,  # User-controlled temperature
            system_prompt=___  # Custom behavior
        ):
            full_response += ___
            message_placeholder.write(full_response + "▌")
        
        message_placeholder.write(___)
    
    # TODO: Save response
    st.session_state.___.append({"role": "___", "content": ___})