from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]       

result = embeddings.embed_documents(documents)
print(str(result))
