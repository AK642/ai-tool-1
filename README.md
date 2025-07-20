# AI Tool 1 - gRPC Microservice

A Python-based gRPC microservice that provides an AI tool interface for processing user messages.

## 🚀 Features

- **gRPC API**: High-performance RPC communication
- **Docker Support**: Containerized deployment
- **Concurrent Processing**: Thread pool with 10 workers
- **Cross-platform**: Works on Windows, Linux, and macOS

## 📋 Prerequisites

- Python 3.11+
- Docker Desktop
- pip (Python package manager)

## 🛠️ Local Development

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
python main.py
```

The service will start on `localhost:50051`

## 🐳 Docker Deployment

### Build and Run with Docker
```bash
# Build the Docker image
docker build -t ai-tool-1 .

# Run the container
docker run -d -p 50051:50051 --name ai-tool-container ai-tool-1

# Check container status
docker ps

# View logs
docker logs ai-tool-container

# Stop and remove container
docker stop ai-tool-container
docker rm ai-tool-container
```

### Using Docker Compose (Recommended)
```bash
# Start the service
docker-compose up -d

# Stop the service
docker-compose down

# View logs
docker-compose logs -f
```

## 🔌 gRPC Communication

### Service Definition
- **Service**: `AITool`
- **Method**: `ProcessMessage`
- **Port**: `50051`

### Message Format
**Input (UserMessage)**:
```protobuf
message UserMessage {
  string message = 1;
  string user_id = 2;
}
```

**Output (ToolResponse)**:
```protobuf
message ToolResponse {
  string response = 1;
}
```

### Test Client
Run the included test client to verify communication:
```bash
python client.py
```

Example output:
```
Connecting to AI Tool gRPC service in Docker container...
Response from AI Tool: Tool1 says: Hello from Docker container!
Response from AI Tool: Tool1 says: Testing gRPC communication
```

## 🔧 API Usage

### Python Client Example
```python
import grpc
import tool_pb2
import tool_pb2_grpc

# Connect to the service
channel = grpc.insecure_channel('localhost:50051')
stub = tool_pb2_grpc.AIToolStub(channel)

# Create and send request
request = tool_pb2.UserMessage(
    message="Hello AI Tool!",
    user_id="user123"
)

response = stub.ProcessMessage(request)
print(response.response)  # Output: Tool1 says: Hello AI Tool!
```

## 📁 Project Structure

```
ai-tool-1/
├── main.py              # gRPC server implementation
├── tool_pb2.py          # Generated protobuf messages
├── tool_pb2_grpc.py     # Generated gRPC service stubs
├── client.py            # Test gRPC client
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container definition
├── docker-compose.yml   # Docker Compose configuration
├── .dockerignore        # Docker build exclusions
└── README.md            # This file
```

## 🌐 Network Access

The service is accessible on:
- **Local**: `localhost:50051`
- **Docker**: `0.0.0.0:50051` (mapped to host port 50051)
- **Health Check**: Built-in Docker health monitoring

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Ajaykumar Vaghela