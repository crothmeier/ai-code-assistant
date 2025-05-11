# Architecture Overview

![Architecture Diagram](../docs/diagram-placeholder.png)

## Components

| Component | Responsibility | Typical Host |
|-----------|----------------|--------------|
| Orchestrator | Routes requests, performs RAG, chooses model | DL360 Gen10 |
| Model Worker | Serves LLM via HuggingFace TGI | GPU nodes |
| Vector DB | Stores code/document embeddings | DL380p Gen8 |
| Sandbox Executor | Runs generated code in Docker‑in‑Docker | DL380p Gen8 |
| CLI | Developer interface | Laptop / local |

See **security.md** for sandboxing and zero‑trust design.
