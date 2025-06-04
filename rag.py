from langchain_community.document_loaders import UnstructuredPDFLoader
# from langchain_community.document_loaders import OnlinePDFLoader

file_path = "./documents/Academic-Regulations.pdf"
model = "gemma3:4b"

if file_path:
    loader = UnstructuredPDFLoader(file_path=file_path)
    data = loader.load()
    print("file loaded.")
else:
    print("no valid path found.")

preview_content = data[0].page_content
# print(preview_content[:100])

# pdf ingestion done

# data chunking and text extraction section
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print("splitting done.")

# print(f"no. of chunks: {len(chunks)}")
# print(f"sample chunk:\n{chunks[0]}")

# adding vector database
import ollama
ollama.pull("nomic-embed-text")

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-text-embed"),
    collection_name="simple-rag"
)
print("added to vector database.")

