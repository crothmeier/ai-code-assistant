from fastapi import FastAPI, HTTPException
import os, requests, uuid

app = FastAPI(title="AI Assistant Orchestrator")

MODEL_ENDPOINTS = eval(os.getenv("MODEL_ENDPOINTS", "[]"))
VECTOR_DB_URL = os.getenv("VECTOR_DB_URL")

@app.get("/")
def root():
    return {"status": "ok", "models": [m["name"] for m in MODEL_ENDPOINTS]}

@app.post("/ask")
def ask(question: str, project_id: str = "default"):
    # TODO: embed question, query vector DB, select model, stream response
    if not MODEL_ENDPOINTS:
        raise HTTPException(status_code=500, detail="No model endpoints defined")
    model = MODEL_ENDPOINTS[0]
    r = requests.post(f"{model['url']}/generate", json={"prompt": question})
    return {"answer": r.json(), "model": model["name"], "id": str(uuid.uuid4())}
