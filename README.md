# Self‑Hosted AI Code Assistant

A modular, distributed Claude‑Code‑style coding copilot for homelab GPU clusters.
This repository contains all the artifacts needed to run the assistant in **monolith**
mode on a single host *or* in **mesh** mode across a 10 GbE backbone.

> **Hardware reference** – HP DL380p Gen8 (T4), Dell T5610 (A4000), ThinkPad T16 (A2000 eGPU), HPE DL360 Gen10 (L4).

## Quick start (single‑node)

```bash
git clone https://github.com/lazarus‑labs/ai‑code‑assistant.git
cd ai‑code‑assistant
docker compose up -d
./cli/assistant ask "Generate a Python Fibonacci function"
```

## Production (mesh) deploy

* Deploy a k3s cluster (or K8s) on all nodes.
* Apply manifests in [`k8s/`](k8s/) – use node selectors so GPU pods land on GPU hosts.
* Mount the NFS share exported by the DL380p on **/mnt/ai‑share** of every node.
* Point the CLI to the orchestrator service DNS name (default `assistant-orchestrator.svc.cluster.local`).

See **docs/** for full architecture, security model, and tuning guides.
