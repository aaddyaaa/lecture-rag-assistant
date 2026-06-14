# AI Lecture Assistant - Retrieval Augmented Generation (RAG) System

## Overview

AI Lecture Assistant is an end-to-end Retrieval-Augmented Generation (RAG) system that enables users to ask questions about lecture videos and receive context-aware answers grounded in the lecture content.

The system processes lecture videos, converts speech into text, generates semantic embeddings for transcript chunks, retrieves the most relevant content using vector similarity search, and produces accurate answers using a locally hosted Large Language Model (LLM).

Unlike traditional chatbots that rely solely on model knowledge, this application retrieves relevant lecture information before generating responses, significantly reducing hallucinations and improving answer relevance.

---

## Key Features

* Automatic lecture transcription using Whisper
* Video preprocessing using FFmpeg
* Semantic chunking and embedding generation
* Vector-based retrieval using cosine similarity
* Context-aware question answering
* Local LLM inference using Ollama and Llama 3.2
* Efficient embedding storage using Joblib
* End-to-end offline execution with no API costs

---

## System Architecture

```text
Lecture Video (.mp4)
        │
        ▼
FFmpeg (Audio Extraction)
        │
        ▼
Whisper Transcription
        │
        ▼
Transcript Generation
        │
        ▼
Text Chunking
        │
        ▼
Embedding Generation (bge-m3)
        │
        ▼
Embedding Storage (Joblib)

User Question
        │
        ▼
Question Embedding
        │
        ▼
Cosine Similarity Search
        │
        ▼
Top-K Relevant Chunks
        │
        ▼
Prompt Construction
        │
        ▼
Llama 3.2 (Ollama)
        │
        ▼
Generated Answer
```

---

## Technology Stack

| Category             | Technology    |
| -------------------- | ------------- |
| Programming Language | Python        |
| Video Processing     | FFmpeg        |
| Speech-to-Text       | Whisper       |
| Embedding Model      | bge-m3        |
| Data Processing      | Pandas, NumPy |
| Similarity Search    | Scikit-Learn  |
| Vector Storage       | Joblib        |
| LLM                  | Llama 3.2     |
| Model Serving        | Ollama        |
| API Communication    | Requests      |

---

## Project Workflow

### 1. Video Processing

Lecture videos are first converted from MP4 format to MP3 using FFmpeg.

```bash
ffmpeg -i lecture.mp4 lecture.mp3
```

This step extracts high-quality audio for transcription.

---

### 2. Speech-to-Text Transcription

Audio files are transcribed using Whisper.

Example Output:

```text
Today we will discuss data augmentation techniques.
Data augmentation helps improve model generalization.
```

The generated transcript serves as the knowledge source for the RAG pipeline.

---

### 3. Transcript Chunking

Long transcripts are divided into smaller chunks.

Example:

```text
Chunk 1:
Introduction to Neural Networks

Chunk 2:
Convolutional Neural Networks

Chunk 3:
Data Augmentation Techniques
```

Benefits:

* Better retrieval precision
* Improved embedding quality
* Reduced context length for the LLM

---

### 4. Embedding Generation

Each chunk is transformed into a dense vector representation using the bge-m3 embedding model.

Example:

```python
[0.12, -0.45, 0.91, ...]
```

Embeddings capture semantic meaning rather than relying on exact keyword matches.

---

### 5. Embedding Storage

Generated embeddings and metadata are stored locally using Joblib.

Stored Information:

* Video Number
* Video Title
* Chunk ID
* Transcript Text
* Start Timestamp
* End Timestamp
* Embedding Vector

Example File:

```text
embeddings.joblib
```

This avoids recomputing embeddings during every application startup.

---

### 6. User Query Processing

When a user submits a question:

```text
What is Data Augmentation?
```

The same embedding model converts the question into a vector representation.

---

### 7. Semantic Retrieval

The query embedding is compared against all stored chunk embeddings using cosine similarity.

Cosine Similarity Formula:

cos(θ) = (A · B) / (||A|| ||B||)

Where:

* A = Question Embedding
* B = Chunk Embedding

The highest scoring chunks are selected as relevant context.

---

### 8. Context Construction

Retrieved chunks are combined into a structured prompt.

Example:

```text
Retrieved Context:
Data augmentation increases dataset diversity.
Common techniques include rotation and flipping.

Question:
What is Data Augmentation?
```

---

### 9. Answer Generation

The prompt is sent to Llama 3.2 through Ollama.

API Endpoint:

```text
http://localhost:11434/api/generate
```

The model generates answers strictly grounded in the retrieved lecture content.

---

## Example Query

### User Question

```text
What is Data Augmentation?
```

### Retrieved Context

```text
Data augmentation increases training data diversity.

Common techniques include image rotation,
flipping and cropping.
```

### Generated Answer

```text
Data augmentation is a technique used to increase
the diversity of training data by applying
transformations such as rotation, flipping,
and cropping to existing samples.
```

---

## Challenges Addressed

* Handling transcription inaccuracies
* Determining optimal chunk sizes
* Improving retrieval relevance
* Prompt engineering for grounded responses
* Efficient storage and loading of embeddings
* Integrating local LLM inference pipelines

---

## Future Enhancements

* FAISS-based vector indexing
* ChromaDB integration
* Hybrid Search (BM25 + Embeddings)
* Re-ranking models
* Multi-document retrieval
* Conversation memory
* Streaming responses
* Web interface using Streamlit or React
* Retrieval evaluation framework

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Natural Language Processing (NLP)
* Semantic Search
* Vector Databases Concepts
* Embedding Models
* Information Retrieval
* Prompt Engineering
* Local LLM Deployment
* API Integration
* Data Processing Pipelines
* Machine Learning Systems
* Python Development

---

## Learning Outcomes

This project provided practical experience in building modern AI systems by combining information retrieval techniques with large language models. It demonstrates how retrieval can be used to improve answer quality, reduce hallucinations, and enable question-answering over private datasets.

The architecture closely mirrors production-grade RAG pipelines used in enterprise AI assistants, document search systems, and knowledge management platforms.
