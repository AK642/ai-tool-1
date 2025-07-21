# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .
COPY ai ./ai

# Expose the gRPC port
EXPOSE 50051

# Run the gRPC server
CMD ["python", "main.py"] 