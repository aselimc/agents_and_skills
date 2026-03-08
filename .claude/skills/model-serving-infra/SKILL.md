---
name: model-serving-infra
description: Production model serving. Triton, TorchServe, BentoML. Dynamic batching, autoscaling, health checks.
---

# Model Serving Infrastructure

## Triton Inference Server
```
model_repository/
  my_model/
    config.pbtxt
    1/
      model.onnx
```
Features: dynamic batching, ensemble pipelines, multi-model, GPU sharing.

## Serving Patterns
- **Health checks**: `/v2/health/ready`, `/v2/health/live`
- **Dynamic batching**: accumulate requests, batch inference, split responses
- **Autoscaling**: scale on GPU utilization or request queue depth
- **A/B testing**: route traffic split between model versions
- **Canary rollout**: 5% -> 25% -> 50% -> 100% traffic migration

## Performance
- Pre/post-processing on CPU, inference on GPU
- Use async I/O for non-blocking request handling
- Monitor: p50/p95/p99 latency, throughput (req/s), GPU memory

## Key Libraries
triton-inference-server, torchserve, bentoml, seldon-core
