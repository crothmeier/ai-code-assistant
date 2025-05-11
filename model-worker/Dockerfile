FROM huggingface/text-generation-inference:latest
ENV MODEL_NAME=${MODEL_NAME:-mistral-7b}
CMD ["--model-id", "${MODEL_NAME}", "--port", "8080"]
