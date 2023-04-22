# server.py
import socket

# TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 500))
server.listen()

client_socket, client_address = server.accept()

file = open("image_server.jpg", mode="wb")
data = client_socket.recv(2048)
while data:
    file.write(data)
    data = client_socket.recv(2048)

file.close()
