import streamlit as st
import requests
import json

def stream_ollama_response(messages, model="llama3.2:latest"):
    """Stream response chunk by chunk - Part 7 + streaming!"""
    url = "http://localhost:11434/api/chat"  # Same as Part 7
    
    # TODO: Enable streaming in payload
    payload = {
        "model": model,
        "messages": messages,
        "stream": ___  # Set to True!
    }
    
    try:
        # TODO: Make request with stream=True
        response = requests.post(url, json=payload, stream=___)
        response.raise_for_status()
        
        # TODO: Iterate over each line in the response
        for line in response.___():
            if line:
                # TODO: Parse the JSON chunk
                chunk = json.___(line)
                
                # TODO: Extract and yield the content
                if "___" in chunk and "___" in chunk["___"]:
                    content = chunk["___"]["___"]
                    yield ___
    
    except requests.exceptions.ConnectionError:
        yield "Error: Could not connect to Ollama. Make sure it's running!"
    except requests.exceptions.RequestException as e:
        yield f"Error: Request failed: {str(e)}"
    except Exception as e:
        yield f"Error: {str(e)}"

st.title("⚡ Streaming Chatbot")
st.caption("Building on Part 7 - Adding streaming for real-time responses")

# TODO: Initialize messages (same as Part 7)
if "___" not in st.session_state:
    st.session_state.___ = []

# TODO: Display messages (same as Part 7)
for msg in st.session_state.___:
    with st.chat_message(msg["___"]):
        st.write(msg["___"])

# TODO: Get input (same as Part 7)
prompt = st.chat_input("Type your message...")

if prompt:
    # TODO: Add user message
    st.session_state.___.append({"role": "___", "content": ___})
    with st.chat_message("___"):
        st.write(___)
    
    # TODO: Stream assistant response
    with st.chat_message("assistant"):
        # Create a placeholder for streaming text
        message_placeholder = st.___()  # Use st.empty()!
        full_response = ""
        
        # TODO: Stream the response
        for chunk in ___(st.session_state.___):
            full_response += ___
            # Update placeholder with cursor effect

            message_placeholder.write(full_response + "▌")    st.session_state.___.append({"role": "___", "content": ___})

            # TODO: Save complete response

        # Final update without cursor    
        message_placeholder.write(___)