import streamlit as st
import requests
import gb_assistant.params as params

# FastAPI endpoint URL
api_url = "http://127.0.0.1:8000/prompt"  # Ensure the FastAPI app is running


# Title of the Streamlit app
st.title("Go ahead, ask a question!")

# Display the game name
st.text(f"The game you are playing is: {params.GAME_NAME}")

# Create a form to handle submission with the Enter key
with st.form(key="query_form"):
    # Prompt text box for user input
    user_input = st.text_input("Enter your question:")

    # Submit button
    submit_button = st.form_submit_button("Enter")

    if submit_button:
        if user_input:
            # Send request to FastAPI
            response = requests.get(api_url, params={"prompt": user_input})

            if response.status_code == 200:
                # Display the answer from FastAPI
                answer = response.json().get("Answer", "No answer provided.")
                st.markdown(
                    f"""
                    <div style="background-color:#f0f8ff; color:#000080; padding:15px; border-radius:10px;">
                    <b>Answer:</b> {answer}
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )
            else:
                st.write("Error: Could not retrieve answer from the API.")
        else:
            st.write("Please enter a question.")
