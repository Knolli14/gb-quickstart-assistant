from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gb_assistant.simple_model.model import load_model, create_answer

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
    print(result)

    #answer = result.get("answer", "no answer found")
    #certainty = result.get("certainty", 1.0)

    return {
        'Answer': "worked",
        #'Game_Name': game,
            #NGE: added a key/value pair to retrieve the name of the game that has been identified in the query/retrival process
            #Needs to be connected upstream to ensure that the name of the game is provided from the endpoint
        #'certainty': certainty, # add certainty to the response
    }

# @app.get("/prompt")
# def fancypred(query:str):
#     """returns fancy prediction"""
#     llm=app.state.llm
#     embed_model=app.state.embeder
#     collection=collection_setup("my_collection")
#     answer = gen_answer(embed_model, llm, query, collection)
#     return answer
