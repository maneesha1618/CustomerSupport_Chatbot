from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from config import HUGGINGFACEHUB_API_TOKEN  # Only needed for gated models

def build_qa_chain(retriever):
    # Load tokenizer & model (you can use any model you prefer here)
    tokenizer = AutoTokenizer.from_pretrained(
        "meta-llama/Llama-2-7b-chat-hf",
        use_auth_token=HUGGINGFACEHUB_API_TOKEN
    )

    model = AutoModelForCausalLM.from_pretrained(
        "meta-llama/Llama-2-7b-chat-hf",
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        use_auth_token=HUGGINGFACEHUB_API_TOKEN
    )

    # Create pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.5
    )

    # Wrap with LangChain
    llm = HuggingFacePipeline(pipeline=pipe)

    # Build QA chain
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
