import grpc
import tool_pb2
import tool_pb2_grpc

def run_client():
    # Create a gRPC channel to connect to the server
    channel = grpc.insecure_channel('localhost:50051')
    
    # Create a stub (client)
    stub = tool_pb2_grpc.AIToolStub(channel)
    
    # Create a request message
    request = tool_pb2.UserMessage(
        message="Hello from Docker container!",
        user_id="test_user_123"
    )
    
    try:
        # Make the gRPC call
        response = stub.ProcessMessage(request)
        print(f"Response from AI Tool: {response.response}")
        
        # Test with another message
        request2 = tool_pb2.UserMessage(
            message="Testing gRPC communication",
            user_id="test_user_456"
        )
        
        response2 = stub.ProcessMessage(request2)
        print(f"Response from AI Tool: {response2.response}")
        
    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code()} - {e.details()}")
    
    finally:
        channel.close()

if __name__ == '__main__':
    print("Connecting to AI Tool gRPC service in Docker container...")
    run_client() 