from socket import *
import os
import sys

def help():
    print("help function")

def get(serverName, serverPort, file_name):
    print("get function")

def put(file_name):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    connectionSocket, addr = clientSocket.accept()

    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    clientSocket.send(file_name.encode())
    clientSocket.send(str(file_size).encode())

    data = file.read()
    clientSocket.sendall(data)
    client.send(b"UPLOAD FINISHED")

    

def ls():
    print("list function")

def quit():
    connectionSocket.close()
    print("quit function")