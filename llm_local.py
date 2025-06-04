from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

def get_local_llm():
    pipe = pipeline("text-generation", model="distilgpt2", max_new_tokens=256, do_sample=True)
    return HuggingFacePipeline(pipeline=pipe)
