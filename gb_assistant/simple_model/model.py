from transformers import pipeline
import gb_assistant.params as params
import PyPDF2
import os

game_file = params.GAME_NAME + ".pdf"
abs_path = os.path.join(os.getcwd(), "raw_data", game_file)
#abs_path = "/Users/alayadi/code/Knolli14/gb-quickstart-assistant/raw_data/3 secrets.pdf"

def load_model():
    """Instanciate the text generation model"""
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return qa_pipeline


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF"""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text


def answer_question(model, question:str):
    """Answer the question passed as input"""
    context = extract_text_from_pdf(abs_path)# Extract context from the PDF
    answer = model(question=question, context=context, max_answer_len=50, top_k=5)
    best_answer=""
    for a in answer:
        if len(best_answer) < len(a.get('answer')):
            best_answer=a.get('answer')
    return best_answer
