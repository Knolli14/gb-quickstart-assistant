from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gb_assistant.rag.model import load_model, create_answer

app = FastAPI()
app.state.model = load_model()
# app.state.llm = load_llm()
# app.state.embeder = load_embeder()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    """home page"""
    return {'Greeting': 'This is the API for the BG LLM'}

@app.get("/prompt")
def predict(query:str, game:str):
    """
    return basic prediction along with game name and certainty score
    """
    model= app.state.model

    result = create_answer(model, query, game)
    return result
