---
name: llm-serving
version: 1.0.0
description: Deploy LLMs for inference. vLLM, TGI, quantization for serving, OpenAI-compatible APIs.
---

# LLM Serving

## vLLM (Recommended)
```bash
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3-8B-Instruct \
  --tensor-parallel-size 2 --max-model-len 8192
```
Provides OpenAI-compatible API with PagedAttention, continuous batching.

## Quantization for Serving
| Method | Bits | Speed | Quality | Use Case |
|--------|------|-------|---------|----------|
| FP16 | 16 | Baseline | Best | When memory allows |
| GPTQ | 4 | 2-3x | Good | GPU serving |
| AWQ | 4 | 2-3x | Good | GPU serving |
| GGUF | 2-8 | Varies | Varies | CPU/edge with llama.cpp |

## Key Optimizations
- **PagedAttention**: efficient KV cache management
- **Continuous batching**: handle variable request rates
- **Speculative decoding**: draft model + verify for faster generation
- **Tensor parallelism**: split model across GPUs

## API Design
- Streaming (SSE) for token-by-token output
- OpenAI-compatible endpoint format for drop-in replacement
- Health check, metrics, and graceful shutdown

## Key Libraries
vllm, text-generation-inference, triton-inference-server, llama.cpp
