from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 5001
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connection received from:', addr)

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
        
        errorFile = open('Error404.html', 'rb')
        errorOutputData = errorFile.read()
        connectionSocket.send(errorOutputData)

        connectionSocket.close()
        print("Connection closed\n")