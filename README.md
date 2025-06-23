# College Assistant

A Streamlit-based app that uses **LangChain**, **Ollama**, and **Chroma** to enable semantic search and question answering on the **VIT College Regulations** PDF document using Retrieval-Augmented Generation (RAG).

---

## Features

- Load and process the **VIT College Regulations** PDF document into searchable vector embeddings.
- Use multiple rephrased queries to improve retrieval (via MultiQueryRetriever).
- Answer user questions contextually using a local language model (e.g., Gemma).
- Fully local and privacy-friendly — no cloud APIs required.
- Interactive UI built with Streamlit.

---

## Dependencies

- Python 3.10+
- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io)
- [Ollama](https://ollama.com)
- [Chroma](https://www.trychroma.com)

Check the [requirements.txt](https://github.com/levyashvin/rag_python/blob/main/requirements.txt) for more.

---

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/vit-college-assistant-chat.git
cd vit-college-assistant-chat
````

### 2. Install Python Dependencies

Ensure that you're in the project directory (`vit-college-assistant-chat`). Then, install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Install Ollama & Models

#### 3.1 Install Ollama

Make sure [Ollama](https://ollama.com) is installed and running locally on your machine. You can download and set it up from their official website.

#### 3.2 Pull Required Models

After setting up Ollama, pull the required models. In your terminal, run the following commands:

```bash
ollama pull gemma3:4b
ollama pull nomic-embed-text
```

These commands will pull the necessary models used for generating embeddings and performing semantic search.

### 4. Replace Document (Optional)

The default document (`VIT-Regulations.pdf`) is used in the app. If you want to use your own document, replace the file in the `documents/` folder and update the `DOC_PATH` in the code accordingly.

---

## Customization / Suggestions for Modifications

To modify this app for different documents or enhance performance, you may want to consider making the following changes:

### 1. **Using a Different Document**

To use a different document, replace the current PDF (`VIT-Regulations.pdf`) in the `documents/` folder. You’ll also need to update the path in the code to reflect the new document. Update the `DOC_PATH` variable in the script to the new document path.

For example:

```python
DOC_PATH = "./documents/your-new-document.pdf"
```

### 2. **Modifying the Prompt**

The current prompt is designed to answer questions based on the document. If you want to modify the way the model processes user queries, you can adjust the prompt template.

Locate the `QUERY_PROMPT` variable in the code:

```python
QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate five
    different versions of the given user question to retrieve relevant documents from
    a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}""",
)
```

You can modify the template to fit the style or context of a different document.

### 3. **Changing the Language Model**

If you want to use a more powerful language model or a different model altogether, change the `MODEL_NAME` variable to the desired model. You can find models available in Ollama or LangChain and switch accordingly.

Example for changing the model:

```python
MODEL_NAME = "gemma3:8b"  # Use a larger version of the model
```

### 4. **Improving the Vector Database**

If you're dealing with large documents, consider fine-tuning the vector database creation process. You can adjust the chunk size or overlap in the `RecursiveCharacterTextSplitter` to better suit your document’s size.

For example:

```python
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=500)
```

Adjust the `chunk_size` and `chunk_overlap` based on the length and structure of the new document.
