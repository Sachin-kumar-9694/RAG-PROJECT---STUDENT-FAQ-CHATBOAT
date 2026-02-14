import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.title("Student FAQ Chatbot")

@st.cache_resource
def setup_db():
    loader = PyPDFLoader("AI_notes.pdf")
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(pages)

    embedding = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embedding)

    return db

db = setup_db()

question = st.text_input("Enter your question:")

if question:
    results = db.similarity_search(question)

    if results:
        st.subheader("Answer:")
        st.write(results[0].page_content)
    else:
        st.write("No relevant answer found.")
