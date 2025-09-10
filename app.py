import streamlit as st
from main import load_pipeline  # import the clean one from main.py

st.title("An AI Assistant")
st.markdown("Ask questions about your PDF using **LangChain + FAISS + HuggingFace + Groq**")

# -------------------------------
# Session State
# -------------------------------
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# Load Pipeline Button
# -------------------------------
if st.button("Initialize RAG Pipeline"):
    with st.spinner("Processing PDF and building vector database..."):
        st.session_state.qa_chain = load_pipeline()
    st.success("Pipeline is ready!")

# -------------------------------
# Chat Interface
# -------------------------------
if st.session_state.qa_chain:
    user_question = st.chat_input("Ask a question about the PDF...")

    if user_question:
        with st.spinner("Thinking..."):
            result = st.session_state.qa_chain(
                {"question": user_question, "chat_history": st.session_state.chat_history}
            )
            answer = result["answer"]

        # Save to history
        st.session_state.chat_history.append((user_question, answer))

    # Display Chat History
    for q, a in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(q)
        with st.chat_message("assistant"):
            st.write(a)

else:
    st.info("Click **Initialize RAG Pipeline** to start using the assistant.")

# -------------------------------
# Footer
# -------------------------------
st.markdown(
    "<hr><center>Built by Bipul | Powered by LangChain, FAISS & Streamlit</center>",
    unsafe_allow_html=True
)
