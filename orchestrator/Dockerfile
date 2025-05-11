FROM python:3.10-slim
WORKDIR /app
COPY orchestrator/app /app
RUN pip install fastapi uvicorn[standard] qdrant-client
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
