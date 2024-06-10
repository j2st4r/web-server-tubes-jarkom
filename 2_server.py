from socket import *
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], 'rb')
        outputdata = f.read()
        
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        connectionSocket.send(outputdata)

        connectionSocket.close()
        print("Connection closed\n")
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        
        connectionSocket.close()
        print("Connection closed\n")

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverPort = 5002
    serverSocket.bind(('127.0.0.1', serverPort))
    serverSocket.listen(5)
    print('The server is ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        print('Connection received from:', addr)

        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()
        
    serverSocket.close()

if __name__ == "__main__":
    main()