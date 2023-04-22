# client.py
import socket
import struct

# TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 500))

file = open("image.jpg", mode="rb")
data = file.read(2048)
while data:
    client.send(data)
    data = file.read(2048)

file.close()
client.close()
