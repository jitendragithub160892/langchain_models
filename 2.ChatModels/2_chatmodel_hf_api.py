from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint


llm = HuggingFaceEndpoint(  
repo_id="meta-llama/Meta-Llama-3-8B-Instruct",  
huggingfacehub_api_token="your_huggingface_api_key",
task="text-generation",
)  


model= ChatHuggingFace(
    llm=llm
)

result = model.invoke("What is the capital of India?")
print(result.content)