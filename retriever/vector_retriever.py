from langchain.vectorstores import FAISS
from embeddings.embedder import get_embedding_model

def build_or_load_retriever(chunks, persist_path="vector_store/faiss_index"):
    embedding = get_embedding_model()
    try:
        return FAISS.load_local(persist_path, embedding).as_retriever()
    except:
        db = FAISS.from_documents(chunks, embedding)
        db.save_local(persist_path)
        return db.as_retriever()
