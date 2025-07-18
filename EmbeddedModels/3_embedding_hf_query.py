from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text="New Delhi is the capital of India"

result = embeddings.embed_documents(text)
print(str(result))
