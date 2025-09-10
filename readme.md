# Project Documentation: RAG-based AI Assistant

## 1. Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain, FAISS, HuggingFace, and Groq LLMs**.

The application enables users to:

* Upload or use predefined PDFs.
* Ask natural language questions about the PDF.
* Get **context-aware answers** using **vector search + LLM reasoning**.
* Interact with the system through an **attractive Streamlit UI**.

---

## 2. System Architecture

### Project Structure

```
rag_app/
│── app.py                # Streamlit UI
│── main.py               # Entry point for pipeline loading
│── config.py             # Environment configuration
│── pdf_utils.py          # PDF extraction utility
│── text_utils.py         # Text splitting utility
│── vector_utils.py       # FAISS vector database builder
│── rag_pipeline.py       # RAG pipeline setup with Groq LLM
│── requirements.txt      # Dependencies
│── .env                  # Environment variables (PDF_PATH, GROQ_API_KEY)
│── data/
│    └── mental.pdf       # Sample PDF
```

---

## 3. Workflow

### Step 1: PDF Processing

* Extract text using `PyPDF2` (`pdf_utils.py`).
* Split into smaller overlapping chunks with `RecursiveCharacterTextSplitter` (`text_utils.py`).

### Step 2: Vector Embeddings

* Generate embeddings using HuggingFace’s **all-MiniLM-L6-v2** model (`vector_utils.py`).
* Store embeddings in a **FAISS** vector database for efficient retrieval.

### Step 3: RAG Pipeline Setup

* Integrate **retriever (FAISS)** with **Groq LLM** (`rag_pipeline.py`).
* Use **ConversationalRetrievalChain** to handle contextual Q\&A.

### Step 4: Streamlit UI

* Button to **Initialize RAG Pipeline**.
* Chat-like interface (`st.chat_input`) for Q\&A.
* Maintains **chat history** in `st.session_state`.

---

## 4. Technology Stack

| Component         | Technology Used            |
| ----------------- | -------------------------- |
| Programming Lang  | Python 3.10+               |
| LLM               | Groq (openai/gpt-oss-120b) |
| Vector DB         | FAISS                      |
| Embeddings        | HuggingFace (MiniLM)       |
| Framework         | LangChain                  |
| UI                | Streamlit                  |
| PDF Parser        | PyPDF2                     |
| Config Management | dotenv                     |

---

## 5. Key Features

Retrieval-Augmented Generation (RAG)
Support for any PDF document
Context-aware conversational memory
Interactive Streamlit interface
Modular and scalable code architecture

---

## 6. How to Run

### Prerequisites

* Python 3.10+
* Install dependencies:

```bash
pip install -r requirements.txt
```

* Add **.env** file:

```
PDF_PATH=./data/mental.pdf
GROQ_API_KEY=your_api_key_here
```

### Run the Streamlit App

```bash
streamlit run app.py
```

---

## 7. User Interface

* **Initialize RAG Pipeline Button** → loads PDF, creates embeddings, and initializes LLM.
* **Chat Window** → users type questions about the PDF.
* **Chat History** → keeps track of Q\&A context.
* **Footer Branding** → “Built by Bipul | Powered by LangChain, FAISS & Streamlit”.

---

## 8. Future Enhancements

* Multi-PDF support.
* Deploy on AWS/GCP/Azure with containerization.
* Analytics Dashboard (e.g., most asked questions).
* Voice input for queries.
* Mobile-friendly UI.

---

## 9. Diagram

Here’s a simple **high-level architecture diagram** (can also make a better version in draw\.io, LucidChart, or Mermaid):

```
       ┌────────────┐
       │   PDF Doc   │
       └─────┬──────┘
             │
             ▼
   ┌───────────────────┐
   │   PDF Extractor    │
   │   (PyPDF2)         │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │   Text Splitter    │
   │   (LangChain)      │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │  Embeddings + DB   │
   │ (HuggingFace+FAISS)│
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Conversational RAG │
   │ (Groq LLM + Chain) │
   └─────────┬─────────┘
             │
             ▼
   ┌───────────────────┐
   │ Streamlit UI Chat  │
   └───────────────────┘
```

---

## 10. Credits

Developed by **Bipul Kumar**
Powered by **LangChain, HuggingFace, Groq, FAISS, and Streamlit**

