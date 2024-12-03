import streamlit as st
import requests
import gb_assistant.params as params

# FastAPI endpoint URL
api_url = "http://127.0.0.1:8000/prompt"  # Ensure the FastAPI app is running


# Title of the Streamlit app
st.title("You need help with a game?")
st.title("Welcome to the BG Assistant - this is the place where you find your answer")

# commented this out. reason: game name will be identified by query/retrival process
# Display the game name
#st.text(f"The game you are playing is: {params.GAME_NAME}") #To Do: replace params.Game_Name with actual game that is retrieved

# Create a form to handle submission with the Enter key
with st.form(key="query_form"):
    # Prompt text box for user input
    st.text(
        "What do you need to know?\n\n...and don't tell me what game you are playing - that is my job :-)"
        )
    user_input = st.text_input("")

    # Submit button
    submit_button = st.form_submit_button("Enter")

    if submit_button:
        if user_input:
            # Send request to FastAPI
            with st.spinner("Finding the perfect answer for you..."): # this creates a loading animation
                try:
                    response = requests.get(api_url, params={"query": user_input}, timeout=60)

                    if response.status_code == 200:
                        # Parse the JSON response
                        response_data = response.json()
                        # Display the answer from FastAPI
                        answer = response_data.get("Answer", "No answer provided.")
                        game_name = response_data.get("game_name", "We don't have that game in our library") # NGE: added this line to also retrieve the game name, needs to be connected upstream
                        certainty = 1.0 # hard-coded certainty to 1.0 so that below if/else statement evaluates to else. After implementing changes to fast.py use code line below
                        #cerainty = response_data.get("certainty", 1.0) # Assuming certainty score is part of the response, need to update fast.py for this

                        # check for certainty score
                        if certainty < 0.01: #value set deliberately low, so wont throw an erro in the beginnging. TO DO: Threshold will need to be set later
                            st.warning("We need more details to identify the game you are playing.")
                            with st.expander("Click here to provide more details to the game you are playing"):
                                additional_info = st.text_area("Describe the question in more detail")

                                # Add a submit button for another API call
                                if st.button("Submit Additional Info"):
                                    # Make a follow-up API call with additional info
                                    follow_up_response = request.get(
                                        api_url,
                                        params={"query": additional_info, "context": user_input},
                                        timeout=60,
                                    )
                                    if follow_up_response.status_code == 200:
                                        follow_up_data = follow_up_response.json()
                                        clarification_answer = follow_up_data.get("Answer", "No clarification provided :-(.")
                                        st.success(f"Clarified Answer: {clarification_answer}")
                                    else:
                                        st.error("Error retrieving clarification response from API.")
                        else:
                            # display the answer if certainty is acceptable
                            st.markdown(
                                f"""
                                <div style="background-color:#f0f8ff; color:#000080; padding:15px; border-radius:10px;">
                                <b>Answer:</b> {answer}
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )
                            st.balloons()
                    else:
                        st.write("Error: Could not retrieve answer from the API.")
                except Exception as e:
                        st.error(f"An error occurred: {e}")
        else:
            st.write("Please enter a question.")
