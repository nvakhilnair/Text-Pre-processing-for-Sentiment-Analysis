# Use a minimal base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app into the container
COPY . .

# Expose the port the FastAPI app runs on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000", "--workers", "1", "--no-proxy-headers", "--limit-concurrency", "5", "--backlog", "5", "--timeout-graceful-shutdown", "30"]
