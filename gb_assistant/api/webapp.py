import streamlit as st
import requests
import gb_assistant.params as params

# FastAPI endpoint URL
api_url = "http://127.0.0.1:8000/prompt"  # Ensure the FastAPI app is running


# Title of the Streamlit app
st.title("Do you need help with a game?")
st.title("Welcome to the BG Assistant - this is the place where you find your answer")


# List of games
# TODO: add games list
games_list = ["kingdomino", "battle sheep", "dr eureka", "codenames", "when i dream", "unlock escape adventures", "terraforming mars", "7 wonders duel", "exploding kittens", "this war of mine the board game", "queendomino", "7 wonders"]


# Dynamic game suggestion input
st.text("Start typing the game you are playing:")
game_input = st.text_input("Game Name")


# Filter the game dynamically
if game_input:
    filtered_games = [game for game in games_list if game_input.lower() in game.lower()]
else:
    filtered_game = st.selectbox("Select the game from the suggestions:", filtered_games)


#Show filtered games in a dropdown
if filtered_games:
    selected_game = st.selectbox("Select the game from the suggestions:", filtered_games)
else:
    st.warning("No matching game found. Please try typing a different name.")
    selected_game = None # Ensure no game is selected if none match


# Create a form to handle submission with the Enter key
with st.form(key="query_form"):
    # Prompt text box for user input
    st.text("What do you need to know?")
    user_input = st.text_input("")

    # Submit button
    submit_button = st.form_submit_button("Enter")

    if submit_button:
        if user_input:
            # Send request to FastAPI
            with st.spinner("Finding the perfect answer for you..."): # this creates a loading animation
                try:
                    response = requests.get(
                        api_url,
                        params={"query": user_input, "game": selected_game},
                        timeout=60
                        )

                    if response.status_code == 200:
                        # Parse the JSON response
                        response_data = response.json()
                        # Display the answer from FastAPI
                        answer = response_data.get("Answer", "No answer provided.")
                        st.balloons()
                    else:
                        st.write("Error: Could not retrieve answer from the API.")
                except Exception as e:
                        st.error(f"An error occurred: {e}")
        else:
            st.write("Please enter a question.")
