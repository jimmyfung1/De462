import streamlit as st
import requests

def chat_with_ollama(messages, model="llama3.2:latest"):
    """Use Ollama's chat API - simpler than Part 6!"""
    
    # TODO: Set the correct chat API endpoint (not /api/generate!)
    url = "http://localhost:11434/api/___"
    
    # TODO: Create payload with messages (no manual formatting!)
    payload = {
        "___": model,
        "___": messages,  # Send messages list directly!
        "stream": False
    }
    
    try:
        response = requests.post(url, json=___)
        response.raise_for_status()
        result = response.json()
        
        # TODO: Extract content from the correct location
        # Hint: result["message"]["content"]
        if "___" in result and "___" in result["___"]:
            return result["___"]["___"]
        else:
            return f"Error: Unexpected response format"
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure it's running!"
    except requests.exceptions.RequestException as e:
        return f"Error: Request failed: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

st.title("💬 Chat API Chatbot")
st.caption("Building on Part 6 - Using /api/chat instead of /api/generate")

# TODO: Initialize messages (same as Part 6)
if "___" not in st.session_state:
    st.session_state.___ = []

# TODO: Display messages (same as Part 6)
for msg in st.session_state.___:
    with st.chat_message(msg["___"]):
        st.write(msg["___"])

# TODO: Get input (same as Part 6)
prompt = st.chat_input("Your message...")

if prompt:
    # TODO: Add user message
    st.session_state.___.append({"___": "___", "___": ___})
    with st.chat_message("___"):

        st.write(___)    st.session_state.___.append({"___": "___", "___": ___})

        # TODO: Save response

    # TODO: Get response using chat API    

    with st.chat_message("assistant"):        st.write(___)

        with st.spinner("Thinking..."):            response = ___(st.session_state.___)
            # Pass messages directly - much simpler than Part 6!