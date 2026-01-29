import streamlit as st
import requests
import json

def get_ollama_response(prompt, model="llama3.2:latest"):
    """Call Ollama API and return response with proper error handling"""
    
    # TODO: Set the correct Ollama API URL
    url = "http://localhost:___/api/___"
    
    # TODO: Complete the payload dictionary
    payload = {
        "___": model,
        "___": prompt,
        "stream": ___  # Set to False for now
    }
    
    try:
        # TODO: Make POST request to Ollama
        response = requests.___(url, json=___)
        
        # TODO: Check if request was successful (raises exception for 4xx/5xx)
        response.___()
        
        # TODO: Parse the JSON response
        result = response.___()
        
        # TODO: Check if "response" key exists and return it
        if "___" in result:
            return result["___"]
        else:
            return f"Error: Unexpected response format: {result}"
    
    # TODO: Handle ConnectionError (Ollama not running)
    except requests.exceptions.___:
        return "Error: Could not connect to Ollama. Make sure Ollama is running on http://localhost:11434"
    
    # TODO: Handle RequestException (HTTP errors like 404, 500)
    except requests.exceptions.___ as e:
        return f"Error: Request failed: {str(e)}"
    
    # TODO: Handle any other exceptions
    except Exception as e:
        return f"Error: {str(e)}"

# TODO: Test the function with a Streamlit interface
st.title("🧪 Test Ollama Connection")
test_prompt = st.text_input("Enter a test prompt:", "Say hello in one sentence")

if st.button("Test Connection"):
    with st.spinner("Connecting to Ollama..."):
        response = get_ollama_response(___)
        st.write("**Response:**")
        st.write(response)