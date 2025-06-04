from langchain.chains import RetrievalQA
from vector_store import load_faiss_index
from llm_local import get_local_llm

def create_qa_chain():
    llm = get_local_llm()
    vectorstore = load_faiss_index()
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
