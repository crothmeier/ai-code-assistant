# Lazarus-Labs AI Code Assistant

[![CI](https://img.shields.io/github/actions/workflow/status/Lazarus-Labs/ai-code-assistant/ci.yml?branch=main)]()
[![License](https://img.shields.io/github/license/Lazarus-Labs/ai-code-assistant)]()

## Quick Start (Kubernetes)

```bash
helm repo add lazarus-labs https://lazarus-labs.github.io/helm-charts
helm repo update
helm install ai-assistant lazarus-labs/ai-code-assistant \
  --set modelWorker.resources.limits.nvidia\.com/gpu=1
kubectl port-forward svc/ai-assistant-orchestrator 8000:8000
curl -X POST http://localhost:8000/api/code/complete -d '{"prompt":"FizzBuzz in Go"}'
```
