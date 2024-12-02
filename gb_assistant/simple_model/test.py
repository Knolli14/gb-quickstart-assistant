from gb_assistant.simple_model.chroma import get_collection, setup_chromadb
from gb_assistant.simple_model.llm import load_llm, load_embeder
from gb_assistant.simple_model.main import gen_answer
import chromadb



collection = get_collection()
query = "what is the objective of the game?"

llm = load_llm()
embeder = load_embeder()
answer = gen_answer(embeder, llm, query, collection)

print(answer)
