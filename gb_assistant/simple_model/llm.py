import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from transformers import pipeline

def load_pdfs(pdf_folder_path):
    """loads the pdf"""
    page_documents = []
    for file in os.listdir(pdf_folder_path):
        print(file, "being loaded")
        if file.endswith('.pdf'):

            pdf_path = os.path.join(pdf_folder_path, file)
            loader = PyPDFLoader(pdf_path)

            page_documents.extend(loader.load())

    return page_documents

def split_text(page_documents):
    """splits the text"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=768, chunk_overlap=64)
    splits = text_splitter.split_documents(page_documents)
    return splits

def load_embeder():
    """loads the embedding model"""
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return model

def embed(splits):
    """embeds the splitted text"""
    model = load_embeder()
    embeddings = []
    titles = []
    docs = []
    for split in splits:
        text = split.page_content
        embeddings.append(model.encode(text))
        docs.append(text),
        titles.append({
            "game_title": split.metadata["source"].split("/")[-1].strip(".pdf")
        })

    return embeddings, titles, docs

def load_llm():
    """loads the final llm"""
    model_name = "HuggingFaceH4/zephyr-7b-beta"
    qa_pipe = pipeline("text-generation", model=model_name)
    return qa_pipe

a= load_llm()
print(a)
