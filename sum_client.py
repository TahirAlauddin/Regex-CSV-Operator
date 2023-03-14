from socket import socket, AF_INET, SOCK_STREAM

host = 'localhost'
port = 9876
def connect():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host,port))
    data = client.recv(1024).decode()
    print("Information returned from server:")
    print(data)
    print("Connection to server closed")

connect()