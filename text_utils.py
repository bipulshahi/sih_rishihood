from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
    docs = splitter.create_documents([text])
    return docs
