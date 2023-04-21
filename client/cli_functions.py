from socket import *
import time
import os
import sys

def help():
    print("help function")

def download(serverName, serverPort, file_name):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.bind(('localhost', 5001))
    dataSocket.listen()

    connectionSocket, addr = dataSocket.accept()

    file_name = connectionSocket.recv(1024).decode()
    print("FILE NAME: " + file_name)
    file_size = connectionSocket.recv(1024).decode()

    file = open(file_name, "wb")

    file_bytes = b""

    done = False
    print("Sending File...")
    while not done:
        data = connectionSocket.recv(1024)
        if file_bytes[-3:] == b"EOF":
            done = True
        else:
            file_bytes += data
            print("Bytes recieved: " + str(len(file_bytes)) + "out of " + file_size, end="\r") 

    file.write(file_bytes[0:-3])
    file.close()
    dataSocket.close()

def upload(serverName, serverPort, file_name):
    time.sleep(1)
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect(('localhost', 5001))

    print("FILE NAME:" + file_name)

    file = open(file_name, "rb")
    file_size = os.path.getsize(file_name)

    dataSocket.send(file_name.encode())
    dataSocket.send(str(file_size).encode())

    data = file.read()
    dataSocket.sendall(data)
    dataSocket.send(b"EOF")
    file.close()
    dataSocket.close()

    

def ls(serverName, serverPort):
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect(('localhost', 5001))
    dataSocket.listen()
    connectionSocket, addr = dataSocket.accept()

    data = connectionSocket.recv(1024)
    file_names = pickle.loads(data)
    print(file_names)
    dataSocket.close()

def quit():
    print("quit function")