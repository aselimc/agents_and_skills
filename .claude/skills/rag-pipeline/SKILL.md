---
name: rag-pipeline
version: 1.0.0
description: Retrieval-Augmented Generation. Chunking, embedding, vector stores, retrieval, and generation.
---

# RAG Pipeline

## Architecture
```
Documents -> Chunking -> Embedding -> Vector Store -> Retrieval -> LLM Generation
```

## Chunking Strategies
- **Fixed-size**: 512 tokens with 50-token overlap
- **Recursive**: split by `\n\n` > `\n` > `. ` > ` ` until chunk_size met
- **Semantic**: split by topic/section boundaries

## Embedding & Retrieval
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)
# Store in FAISS/Qdrant/Chroma
```

## Hybrid Retrieval (Best Practice)
1. BM25 keyword search (sparse)
2. Dense vector search (semantic)
3. Reciprocal rank fusion to merge results
4. Cross-encoder re-ranking on top-k

## Rules
- Chunk size should match embedding model's context window
- Always include source metadata for attribution
- Evaluate: retrieval recall@k, answer accuracy, faithfulness
- Guard against prompt injection in retrieved content

## Key Libraries
langchain, llama-index, sentence-transformers, FAISS, chromadb
