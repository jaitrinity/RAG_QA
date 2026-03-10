import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Agentic Document Q&A System")

st.header("Upload PDF")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:

    files = {"file": uploaded_file}

    res = requests.post(f"{API_URL}/upload", files=files)

    st.success(res.json())


st.header("Ask Question")

question = st.text_input("Enter your question")

if st.button("Ask"):

    response = requests.post(
        f"{API_URL}/ask",
        json={"question": question}
    )

    result = response.json()

    st.subheader("Agent Reasoning")
    st.write(result["agent_reasoning"])

    st.subheader("Retrieved Context")
    st.write(result["retrieved_context"])

    st.subheader("Answer")
    st.write(result["answer"])