import streamlit as st

# TODO: Initialize 'click_count' in session state to 0 if it doesn't exist
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

st.title("My First Interactive App")

# TODO: Create a text input widget to get the user's name
# Hint: use st.text_input()
user_name = st.text_input("What's your name?")

# TODO: Display a greeting if the user entered a name
# Hint: use st.write() and f-string
if user_name:
    st.write(f"My name is, {user_name}!")

# TODO: Create a button and increment the counter when clicked
if st.button("Enter Your Name"):
    st.session_state.click_count += 1
    
# TODO: Display the current count
st.write(f"Button clicked {st.session_state} times")