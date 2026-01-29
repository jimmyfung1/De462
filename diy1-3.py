import streamlit as st

st.title("🔄 Reverse Echo Chatbot")

# TODO: Initialize messages list in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# TODO: Display all previous messages
for message in st.session_state.___:
    with st.chat_message(st.message["role"]):
        st.write(message["content"])

# TODO: Get user input
prompt = st.chat_input("Say something...")

if prompt:
    # TODO: Add user message to session state
    st.session_state.message.append({"role": "user", "content": prompt})
    
    # TODO: Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # TODO: Create reversed response (reverse the string)
    response = f"Reversed: {prompt[::-1]}"
    
    # TODO: Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # TODO: Display assistant response
    with st.chat_message("assistance"):
        st.write(response)