import streamlit as st
import sys
import os

# Set path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
load_dotenv()

from loaders.document_loader import load_and_split_docs
from retriever.vector_retriever import build_or_load_retriever
from llm.rag_chain import build_qa_chain

# Set Streamlit title
st.title("🛍️ Customer Support Chatbot")

# Load and process docs
docs = load_and_split_docs("data/ecommerce_faq.md")
retriever = build_or_load_retriever(docs)
qa_chain = build_qa_chain(retriever)

# Input from user
query = st.text_input("Ask a question:")

if query:
    with st.spinner("Thinking..."):
        response = qa_chain.invoke({"query": query})

        # Handle dictionary response properly
        answer = response.get("result", "Sorry, I couldn't find an answer.")
        st.write("🤖", answer)

        # Optional: show sources
        with st.expander("Show sources"):
            for i, doc in enumerate(response.get("source_documents", []), 1):
                st.markdown(f"**Source {i}:**\n{doc.page_content}")


# llm/rag_chain.py

# from langchain_community.llms import HuggingFacePipeline
# from transformers import pipeline
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate

# def build_qa_chain(retriever):
#     # Load a model (e.g., Falcon, Mistral, or any smaller one for local usage)
#     qa_pipeline = pipeline(
#         "text-generation",
#         model="tiiuae/falcon-7b-instruct",  # or another suitable model
#         tokenizer="tiiuae/falcon-7b-instruct",
#         max_new_tokens=256,
#         temperature=0.7,
#         do_sample=True
#     )

#     llm = HuggingFacePipeline(pipeline=qa_pipeline)

#     # Define a prompt template
#     prompt = PromptTemplate.from_template("""
#     You are a helpful assistant. Use the context to answer the question.
#     Context: {context}
#     Question: {question}
#     Answer:
#     """)

#     # Combine into a retrieval-based QA chain
#     qa_chain = RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         chain_type="stuff",
#         chain_type_kwargs={"prompt": prompt},
#         return_source_documents=True
#     )

#     return qa_chain
