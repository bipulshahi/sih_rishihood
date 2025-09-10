from config import PDF_PATH, GROQ_API_KEY
from pdf_utils import extract_data_from_pdf
from text_utils import split_text
from vector_utils import create_vector_store
from rag_pipeline import setup_rag_qa

def load_pipeline():
    text = extract_data_from_pdf(PDF_PATH)
    docs = split_text(text)
    vectorstore = create_vector_store(docs)
    return setup_rag_qa(vectorstore, GROQ_API_KEY)

if __name__ == "__main__":
    qa_chain = load_pipeline()
    query = input("Enter Your Query: ")
    result = qa_chain.run(query)
    print("\nAnswer:", result)
