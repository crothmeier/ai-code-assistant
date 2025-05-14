# Security Model

1. **Zero‑trust code execution** – every `run` request spawns
   a one‑shot Docker container with:

   - No outbound network
   - CPU/memory/time quotas
   - Mounted `/workspace` tmpfs only

2. **Project isolation** – vector collections are namespaced
   by project ID. Orchestrator enforces JWT‑scoped access.

3. **Transport security** – all gRPC within cluster uses mTLS
   via cert‑manager if on K8s, or WireGuard on bare‑metal.
