from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gb_assistant.simple_model.model import load_model, answer_question

app = FastAPI()
app.state.model = load_model()

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
    return {'Greeting': 'This is the API for the BG LLM'}

@app.get("/prompt")
def predict(prompt:str):
    model= app.state.model
    return {'Answer':answer_question(model, prompt)}
