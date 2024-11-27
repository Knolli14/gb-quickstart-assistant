import streamlit as st
import requests

# FastAPI endpoint URL
api_url = "http://127.0.0.1:8000/prompt"  # Make sure the FastAPI app is running

# Title of the Streamlit app
st.title("Query Interface for FastAPI")

# Prompt text box for user input
user_input = st.text_input("Enter your question:")

# Submit button
if st.button("Submit"):
    if user_input:
        # Send request to FastAPI
        response = requests.get(api_url, params={"prompt": user_input})

        if response.status_code == 200:
            # Display the answer from FastAPI
            answer = response.json().get("Answer", "No answer provided.")
            st.write(f"Answer: {answer}")
        else:
            st.write("Error: Could not retrieve answer from the API.")
    else:
        st.write("Please enter a question.")
