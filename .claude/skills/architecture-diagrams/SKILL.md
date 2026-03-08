---
name: architecture-diagrams
version: 1.0.0
description: Generate Mermaid diagrams for system architecture, data flows, class hierarchies, and API sequences.
---

# Architecture Diagrams

## System Architecture (C4 Style)
```mermaid
graph LR
    Client --> API[API Gateway]
    API --> Auth[Auth Service]
    API --> ML[ML Service]
    ML --> Model[Model Registry]
    ML --> GPU[GPU Cluster]
```

## Sequence Diagram
```mermaid
sequenceDiagram
    Client->>+API: POST /predict
    API->>+ModelService: inference(input)
    ModelService->>+GPU: forward pass
    GPU-->>-ModelService: output
    ModelService-->>-API: prediction
    API-->>-Client: 200 OK
```

## Class Diagram
```mermaid
classDiagram
    class BaseModel { +forward(x) +save() +load() }
    class Encoder { +encode(x) }
    class Decoder { +decode(z) }
    BaseModel <|-- Encoder
    BaseModel <|-- Decoder
```

## Rules
- Max ~15 nodes per diagram (split if larger)
- Clear, descriptive labels (no abbreviations without context)
- Use `graph TD` for vertical, `graph LR` for horizontal
- Always wrap in ```mermaid code blocks
