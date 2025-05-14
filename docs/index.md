# AI Code Assistant

A FastAPI-based AI code assistant with GPU-aware routing for efficient resource allocation.

## Overview

The AI Code Assistant is a platform for deploying and managing AI coding assistants with intelligent GPU selection and resource allocation. It uses a weighted routing system to direct requests to the most appropriate GPU based on model requirements and resource availability.

Key features:

- **GPU-aware routing**: Automatically selects the optimal GPU for each request
- **Weighted load balancing**: Distributes workload based on GPU capability
- **Kubernetes integration**: Seamlessly runs in Kubernetes environments
- **Monitoring**: Prometheus metrics for performance tracking
- **Security**: Robust security controls and container hardening

## Quick Start

### Prerequisites

- Python 3.11+
- Poetry for dependency management
- Docker and Docker Compose for containerization (optional)
- Kubernetes for production deployment (optional)

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/crothmeier/ai-code-assistant.git
   cd ai-code-assistant
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Run the tests**:
   ```bash
   poetry run pytest
   ```

4. **Start the development server**:
   ```bash
   poetry run uvicorn orchestrator.app:app --reload
   ```

5. **Access the API**:
   - API will be available at http://localhost:8000
   - Documentation at http://localhost:8000/docs

### Using Docker

```bash
# Build and start the services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the services
docker-compose down
```

### Kubernetes Deployment

```bash
# Apply the network policy for DNS
kubectl apply -f k8s/netpol-allow-dns.yaml

# Deploy the orchestrator
kubectl apply -f k8s/orchestrator-deployment.yaml

# Check deployment status
kubectl get pods -l app=orchestrator
```

## Project Structure

```
ai-code-assistant/
├── charts/                  # Helm charts
├── docs/                    # Documentation
├── k8s/                     # Kubernetes manifests
├── model-worker/            # Model worker implementation
├── orchestrator/            # Main orchestration service
├── sandbox-executor/        # Sandbox execution environment
├── src/                     # Core source code
│   └── router/              # Routing logic
└── tests/                   # Unit and integration tests
```

## Next Steps

- Check out the [Router Design](router.md) documentation
- Review the [Security](security.md) practices
- Explore the [Architecture](architecture.md) overview
