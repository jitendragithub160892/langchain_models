from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# import os


llm = HuggingFaceEndpoint(  
repo_id="meta-llama/Meta-Llama-3-8B-Instruct",  
huggingfacehub_api_token="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",
# huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
task="text-generation",
)  


model= ChatHuggingFace(
    llm=llm
)

result = model.invoke("What is the capital of India?")
print(result.content)