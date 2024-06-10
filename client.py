from socket import *
import sys

def http_client(server_host, server_port, path):
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect((server_host, server_port))

    request = f"GET {path} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
    print(request)
    client_socket.sendall(request.encode())

    response = b""
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part

    client_socket.close()

    print(response.decode())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 client.py <server_host> <server_port> <path>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    path = sys.argv[3]
    
    http_client(server_host, server_port, path)