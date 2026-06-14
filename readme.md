# AI Course Q&A System (RAG Pipeline)

## Overview

This project is a **Retrieval-Augmented Generation (RAG)** based AI assistant that answers questions about lecture videos.

Instead of relying solely on the language model's internal knowledge, the system retrieves relevant lecture content from video transcripts and uses that information to generate accurate, context-aware answers.

The project demonstrates the complete workflow of a modern RAG system including:

* Speech-to-Text Transcription
* Text Chunking
* Embedding Generation
* Vector Similarity Search
* Context Retrieval
* LLM-based Answer Generation

---

# Architecture

```text
Lecture Videos
      ↓
Speech-to-Text (Whisper)
      ↓
Transcript
      ↓
Chunking
      ↓
Embeddings (bge-m3)
      ↓
Store Embeddings
      ↓

User Question
      ↓
Question Embedding
      ↓
Cosine Similarity Search
      ↓
Top Relevant Chunks
      ↓
Llama 3.2 (Ollama)
      ↓
Final Answer
```

---

# Technologies Used

| Component         | Technology         |
| ----------------- | ------------------ |
| Speech-to-Text    | Whisper            |
| Embedding Model   | bge-m3             |
| Vector Search     | Cosine Similarity  |
| LLM               | Llama 3.2 (Ollama) |
| Storage           | Joblib             |
| Language          | Python             |
| Data Processing   | Pandas, NumPy      |
| Similarity Search | Scikit-Learn       |
| API Requests      | Requests           |

---

# Project Workflow

## Step 1: Lecture Transcription

Lecture videos are converted into text transcripts using Whisper.

### Input

```text
lecture.mp4
```

### Output

```text
Today we will discuss data augmentation.
Data augmentation increases dataset diversity.
```

### Purpose

* Convert audio into searchable text.
* Create a knowledge base for retrieval.

---

## Step 2: Text Chunking

Large transcripts are divided into smaller chunks.

### Example

```text
Chunk 1:
Introduction to CNNs

Chunk 2:
Data Augmentation Techniques

Chunk 3:
Transfer Learning
```

### Why Chunking?

* Improves retrieval accuracy.
* Produces better embeddings.
* Reduces context size for the LLM.

---

## Step 3: Embedding Generation

Each chunk is converted into a numerical vector using the **bge-m3** embedding model.

### Example

Question:

```text
What is NLP?
```

Embedding:

```python
[0.12, -0.45, 0.91, ...]
```

### Purpose

Embeddings capture the semantic meaning of text, allowing the system to compare concepts rather than exact words.

---

## Step 4: Embedding Storage

Generated embeddings are stored locally using Joblib.

### Stored Information

* Video Title
* Chunk Number
* Timestamps
* Transcript Text
* Embedding Vector

### File

```text
embeddings.joblib
```

### Purpose

Avoids recomputing embeddings every time the system starts.

---

## Step 5: User Query Processing

The user submits a question.

### Example

```text
What is Data Augmentation?
```

The same embedding model (**bge-m3**) converts the question into a vector representation.

---

## Step 6: Similarity Search

The question embedding is compared against all stored chunk embeddings using cosine similarity.

### Formula

```text
cos(θ) = (A · B) / (||A|| ||B||)
```

Where:

* A = Question embedding
* B = Chunk embedding

### Similarity Range

| Value | Meaning   |
| ----- | --------- |
| 1     | Identical |
| 0     | Unrelated |
| -1    | Opposite  |

---

## Step 7: Retrieval

Top-K most relevant chunks are selected.

### Example Retrieved Chunks

```text
Chunk 12:
Data augmentation helps increase training data diversity.

Chunk 13:
Common techniques include rotation and flipping.
```

These chunks become the context for answer generation.

---

## Step 8: Prompt Construction

A structured prompt is built using:

* Retrieved Chunks
* User Question
* Instructions

### Example

```text
Retrieved Chunks:
...

Question:
What is Data Augmentation?

Answer only using the retrieved chunks.
```

---

## Step 9: Answer Generation

The prompt is sent to a locally hosted Llama 3.2 model using Ollama.

### Endpoint

```text
http://localhost:11434/api/generate
```

### Purpose

The LLM:

* Reads retrieved lecture content.
* Understands the question.
* Generates a natural language answer grounded in the retrieved context.

---

# Key Concepts Learned

## Retrieval-Augmented Generation (RAG)

RAG combines:

```text
Retrieval
+
Generation
```

### Benefits

* Reduces hallucinations
* Uses domain-specific knowledge
* Works with private data
* Improves answer reliability

---

## Embeddings

Embeddings are vector representations of text.

Example:

```text
NLP
Natural Language Processing
```

Both phrases generate nearby vectors because they have similar meanings.

---

## Cosine Similarity

Measures semantic similarity between vectors.

Used to identify the most relevant transcript chunks for a given question.

---

## Local LLM Deployment

Implemented using Ollama and Llama 3.2.

### Advantages

* No API costs
* Offline execution
* Faster experimentation
* Full model control

---

# Challenges Faced

* Handling transcription errors from Whisper
* Selecting optimal chunk sizes
* Improving retrieval accuracy
* Designing effective prompts
* Managing embedding storage efficiently
* Integrating local LLM inference

---

# Future Improvements

* Use a dedicated vector database (FAISS, ChromaDB, Pinecone)
* Hybrid Search (Keyword + Semantic Search)
* Metadata Filtering
* Conversation Memory
* Streaming Responses
* Web Interface using Streamlit or React
* Multi-document Retrieval
* Re-ranking Models

---

# Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Natural Language Processing (NLP)
* Embedding Models
* Vector Search
* Prompt Engineering
* Local LLM Deployment
* Python Development
* API Integration
* Information Retrieval Systems

---
