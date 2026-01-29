import streamlit as st
import requests

# Function with error handling (building on Part 4 patterns)
def get_ollama_with_memory(messages, model="llama3.2:latest"):
    """Call Ollama with full conversation history"""
    url = "http://localhost:11434/api/generate"
    
    # TODO: Build conversation string from all messages
    conversation = ""
    for msg in messages:
        # TODO: Set role label based on message role
        role = "___" if msg["role"] == "user" else "___"
        # TODO: Add this message to conversation string
        conversation += f"{___}: {msg['___']}\n"
    
    # TODO: Create the full prompt (conversation + "Assistant:")
    full_prompt = f"{___}___:"
    
    payload = {"model": model, "prompt": ___, "stream": False}
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        
        if "response" in result:
            return result["response"]
        else:
            return f"Error: Unexpected response format"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure it's running!"
    except requests.exceptions.RequestException as e:
        return f"Error: Request failed: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

st.title("🧠 Chatbot with Memory")
st.caption("Building on Part 5 with conversation history")

# TODO: Initialize messages (like Part 5)
if "___" not in st.session_state:
    st.session_state.___ = []

# TODO: Display messages (like Part 5)
for msg in st.session_state.___:
    with st.chat_message(msg["___"]):
        st.write(msg["___"])

# TODO: Get input (like Part 5)
prompt = st.chat_input("Chat with memory...")

if prompt:
    # TODO: Add user message
    st.session_state.___.append({"___": "___", "___": ___})

    with st.chat_message("user"):    st.session_state.___.append({"role": "___", "content": ___})

        st.write(prompt)    # TODO: Save response

        

    # TODO: Get response with memory (pass ALL messages!)        st.write(response)

    with st.chat_message("assistant"):            response = ___(st.session_state.___)

        with st.spinner("Thinking..."):            # Pass ALL messages for context - this is the key!