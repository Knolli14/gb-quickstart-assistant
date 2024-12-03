import os
import gb_assistant.params as params
from gb_assistant.simple_model.chroma import setup_chromadb
from gb_assistant.simple_model.llm import load_pdfs, split_text, embed

game_file = params.GAME_NAME + ".pdf"
abs_path = os.path.join(os.getcwd(), "raw_data", game_file)

def collection_setup(collection_name:str):
    """creartes the collection"""
    pdfs = load_pdfs(abs_path)
    splitted_pdfs = split_text(pdfs)
    embeddings = embed(splitted_pdfs)
    collection = setup_chromadb(collection_name, *embeddings)
    return collection

def prompt_creation(query, query_results):
    """returns prompt"""
    context="\n\n".join(query_results["documents"][0])
    prompt = [
        {"role": "system", "content": "Hi"},
        {"role": "user", "content": context + "\n" + query}
        ]
    return prompt

def gen_answer(embed_model, llm, query, collection):
    """generates an answer"""
    embedded_query = embed_model.encode(query)
    query_results = collection.query(
        query_embeddings = embedded_query,
        n_results=3,
        )
    prompt = prompt_creation(query, query_results)
    tockenized_prompt = llm.tokenizer.apply_chat_template(
        prompt,
        tokenize=False,
        add_generation_prompt=True
        )
    answer = llm(
        tockenized_prompt,
        max_new_tokens=1024,
        #temperatur=0.7,
        )
    return answer
