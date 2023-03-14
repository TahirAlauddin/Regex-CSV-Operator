from socket import socket, AF_INET, SOCK_STREAM
import random
import threading

def sum_random_numbers():

    num1 = abs(random.randint(-100, 100))
    num2 = abs(random.randint(-100, 100))
    num3 = abs(random.randint(-100, 100))
    sum = num1 + num2 + num3
    return f"{num1} + {num2} + {num3} = {sum}"


host = 'localhost'
port = 9876
server = socket(AF_INET, SOCK_STREAM)
server.bind((host,port))
server.listen()

def handle_connections(i):
    while True:
        print(f"Waiting for connection...")
        connection, address = server.accept()
        print(f"... connected from: {address}")
        response = sum_random_numbers()
        connection.send(response.encode())
        connection.close()
        print("Response sent to client")
        print("Client connection closed\n")


threads = []
for i in range(4):
    threading.Thread(target=handle_connections).start()
    