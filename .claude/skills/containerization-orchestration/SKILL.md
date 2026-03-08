---
name: containerization-orchestration
version: 1.0.0
description: Docker multi-stage builds, docker-compose, Kubernetes manifests, Helm, GPU support.
---

# Containerization & Orchestration

## Multi-Stage Dockerfile
```dockerfile
FROM python:3.11-slim AS builder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY src/ /app/src/
USER nonroot
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
CMD ["python", "-m", "app.main"]
```

## Kubernetes Essentials
- Deployment + Service + Ingress for web services
- ConfigMap for config, Secret for credentials
- HPA for autoscaling on CPU/GPU metrics
- Resource limits: always set requests AND limits

## GPU Support
```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```
Requires NVIDIA device plugin and container toolkit.

## Key Libraries
Docker, Kubernetes, Helm, K3s, Balena
