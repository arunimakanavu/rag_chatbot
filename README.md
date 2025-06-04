

# Local RAG Chatbot (JSON-Based with LangChain)

This project implements a simple, local Retrieval-Augmented Generation (RAG) chatbot using LangChain, FAISS for vector search, and a Hugging Face language model (like distilgpt2). It uses a structured JSON file (instead of a PDF) as the knowledge base and allows users to query it via natural language.

Designed to run on machines with 16GB of RAM, this chatbot works entirely offline using local embeddings and a lightweight LLM.

---

## What is Retrieval-Augmented Generation?

RAG combines two powerful ideas:

* Retrieval: find relevant information (context) from a document store (like your JSON catalog).
* Generation: use an LLM to generate an answer based on the retrieved information.

This gives your LLM access to domain-specific data (without retraining!) and ensures answers are grounded in your content.

---

## Project Structure

```
rag_chatbot_json/
├── app.py                  # Command-line chatbot interface
├── chatbot.py              # LangChain pipeline combining LLM + retriever
├── llm_local.py            # Loads a Hugging Face text generation model
├── load_docs.py            # Loads and splits a JSON file into chunks
├── vector_store.py         # Embeds chunks and stores in FAISS vector DB
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
└── data/
    └── catalog.json        # Your custom domain-specific knowledge base
```

---

## catalog.json Format

The chatbot expects catalog.json to be an array of structured entries. Each entry must contain:

* chunk: The main body of text
* metadata: Optional info like source, section, keywords

Example:

```json
[
  {
    "chunk": "Stegosaurs were quadrupedal dinosaurs with plates on their backs...",
    "metadata": {
      "source": "Dinosaurs: A Comprehensive Overview",
      "section": "Stegosaurs",
      "keywords": ["Stegosaurs", "Jurassic", "herbivore"]
    }
  }
]
```

You can customize this to fit your domain (product specs, policies, technical guides, etc.)

---

## How to Run the Chatbot

Step-by-step instructions:

1. Clone this project (or unzip the provided files):

2. Install dependencies:

```bash
pip install -r requirements.txt
pip install jq  # Required for JSONLoader in LangChain
```

3. Add your data:

Place your catalog.json file in the data/ folder.

4. Build the FAISS index:

```bash
python -c "from vector_store import build_faiss_index; build_faiss_index('data/catalog.json')"
```

5. Start the chatbot:

```bash
python app.py
```

Ask a question like:

```
You: What are Stegosaurs?
```

---

## Technologies Used

| Component             | Description                                 |
| --------------------- | ------------------------------------------- |
| LangChain             | Orchestrates the retrieval + LLM pipeline   |
| Hugging Face          | Provides local embedding + text generation  |
| FAISS                 | Vector search engine                        |
| sentence-transformers | Embedding model (all-MiniLM-L6-v2)          |
| distilgpt2            | Lightweight local language model (text-gen) |

All of these run offline, no internet required after setup.

---

## How It Works (Architecture)

1. load\_docs.py loads catalog.json and splits it into semantic chunks.
2. vector\_store.py embeds these chunks and saves them into a FAISS index.
3. app.py allows users to input questions.
4. chatbot.py sets up a LangChain RetrievalQA chain.
5. At runtime:

   * Relevant chunks are retrieved via vector similarity
   * The Hugging Face model generates a natural language answer

---

## Features

* Fully local — runs offline with no external API calls
* Works with structured JSON input (instead of PDFs)
* Uses LangChain's RetrievalQA pipeline
* Lightweight and fast, suitable for laptops
* Easily extensible for other file formats or models

---

## Future Improvements

You can extend this chatbot by:

* Adding a Streamlit or Gradio UI
* Supporting other file types (Markdown, CSV, etc.)
* Using a more powerful local model (e.g., Mistral 7B with quantization)
* Logging user questions and feedback for analysis

---

## Troubleshooting

Q: I get "ImportError: jq not found"
A: Run pip install jq

Q: My chatbot says it doesn’t know the answer
A: Make sure your catalog.json includes relevant chunks and the question matches them semantically.

Q: Getting deprecation warnings?
A: You can future-proof by installing langchain-huggingface and updating your imports:

```bash
pip install -U langchain-huggingface
```

---

## Need Help?

Feel free to reach out or request:

* Help packaging into a GitHub repo
* A sample JSON file
* UI with Streamlit
* Switching to a more powerful LLM

Happy building your RAG chatbot! 🧠✨


