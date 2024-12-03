from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gb_assistant.simple_model.model import load_model, answer_question
#from gb_assistant.simple_model.llm import load_llm, load_embeder
#from gb_assistant.simple_model.main import gen_answer, collection_setup

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
def predict(query:str):
    """return basic prediction"""
    model= app.state.model
    return {'Answer':answer_question(model, query)}

# @app.get("/prompt")
# def fancypred(query:str):
#     """returns fancy prediction"""
#     llm=app.state.llm
#     embed_model=app.state.embeder
#     collection=collection_setup("my_collection")
#     answer = gen_answer(embed_model, llm, query, collection)
#     return answer
