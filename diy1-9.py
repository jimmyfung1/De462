import streamlit as st
import requests
import json
from datetime import datetime

def stream_ollama_response(messages, model="llama3.2:latest"):
    """Stream response - same as Part 8, provided for you"""
    url = "http://localhost:11434/api/chat"
    payload = {"model": model, "messages": messages, "stream": True}
    
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

st.title("🗂️ Multi-Session Chatbot")
st.caption("Building on Part 8 - Managing multiple conversations")

# TODO: Initialize chat_sessions dictionary
if "___" not in st.session_state:
    st.session_state.___ = {
        "___": {  # Default session ID
            "name": "Chat 1",
            "messages": ___,  # Empty list for messages
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    }
    # TODO: Track current active session
    st.session_state.___ = "___"  # Set to default

# Sidebar for session management
with st.sidebar:
    st.header("Chat Sessions")
    
    # TODO: Create new chat button
    if st.button("➕ New Chat"):
        # Generate unique session ID
        session_id = f"session_{len(st.session_state.___)}"
        
        # TODO: Create new session in the dictionary
        st.session_state.___[___] = {
            "___": f"Chat {len(st.session_state.___) + 1}",
            "___": [],
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        # TODO: Switch to the new session
        st.session_state.___ = ___
        st.rerun()
    
    st.divider()
    
    # TODO: List all sessions
    for session_id, session_data in st.session_state.___.items():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # TODO: Button to switch to this session
            if st.button(
                f"💬 {session_data['___']}",
                key=f"btn_{session_id}",
                use_container_width=True
            ):
                st.session_state.___ = ___
                st.rerun()
        
        with col2:
            # TODO: Delete button (only if more than 1 session)
            if len(st.session_state.___) > ___:  # Need at least 1 session
                if st.button("🗑️", key=f"del_{session_id}"):
                    del st.session_state.___[___]
                    # Switch to first available session
                    st.session_state.___ = list(st.session_state.___.keys())[0]
                    st.rerun()
    
    st.divider()
    
    # TODO: Clear current chat button
    if st.button("🧹 Clear Current Chat"):
        st.session_state.___[st.session_state.___]["___"] = []
        st.rerun()

# TODO: Get current session data
current_session = st.session_state.___[st.session_state.___]

# TODO: Display current session info
st.subheader(current_session["___"])
st.caption(f"Created: {current_session['___']} | Messages: {len(current_session['___'])}")

# TODO: Display messages from current session
for message in current_session["___"]:
    with st.chat_message(message["___"]):
        st.write(message["___"])

# TODO: Chat input (same as Part 8)
prompt = st.chat_input("Type your message...")

if prompt:
    # TODO: Add message to current session (not st.session_state.messages!)
    current_session["___"].append({"role": "___", "content": ___})
    with st.chat_message("user"):
        st.write(___)
    
    # TODO: Stream response (same as Part 8, but use current session messages)
    with st.chat_message("assistant"):
        message_placeholder = st.___()  # Create placeholder
        full_response = ""
        
        # Stream using current session's messages
        for chunk in ___(current_session["___"]):
            full_response += ___
            message_placeholder.write(full_response + "▌")
        
        message_placeholder.write(___)
    
    # TODO: Save response to current session
    current_session["___"].append({"role": "___", "content": ___})