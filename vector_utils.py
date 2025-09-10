from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
