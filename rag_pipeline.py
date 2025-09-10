from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq

def setup_rag_qa(vectorstore, groq_api_key):
    # ✅ Updated model (old: llama3-8b-8192 → new: openai/gpt-oss-120b)
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=groq_api_key,
        temperature=0.7
    )
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )
    return qa_chain
