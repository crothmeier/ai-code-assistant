FROM python:3.11-slim AS builder

# Install poetry
RUN pip install --no-cache-dir poetry==1.7.1

# Set up work directory
WORKDIR /app

# Copy only poetry files for dependencies installation
COPY pyproject.toml poetry.lock* ./

# Configure poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies only (without dev dependencies)
RUN poetry install --no-dev --no-interaction --no-ansi

# Second stage for a smaller image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Create user to avoid running as root
RUN addgroup --system app && adduser --system --group app

# Set up the working directory
WORKDIR /app

# Copy dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY . .

# Set ownership of the application files
RUN chown -R app:app /app

# Switch to non-root user
USER app

# Run the application
EXPOSE 8000
CMD ["uvicorn", "orchestrator.app:app", "--host", "0.0.0.0", "--port", "8000"]
