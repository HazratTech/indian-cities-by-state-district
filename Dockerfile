FROM python:3.12-slim

WORKDIR /app

# Install system dependencies if any are needed (minimal image)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
RUN pip install --no-cache-dir fastapi uvicorn

# Copy application files
COPY main.py app.py combined_data.json /app/

# Expose port
EXPOSE 8282

# Start application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8282"]
