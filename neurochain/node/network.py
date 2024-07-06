import socket

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.send(data)

    def receive(self):
        return self.socket.recv(1024)
