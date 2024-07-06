import socket
import threading
import json

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peers = []
        self.lock = threading.Lock()

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send(self, data):
        self.socket.send(json.dumps(data).encode())

    def receive(self):
        return json.loads(self.socket.recv(1024).decode())

    def broadcast(self, data):
        with self.lock:
            for peer in self.peers:
                peer.send(data)

    def add_peer(self, peer):
        with self.lock:
            self.peers.append(peer)

    def start_listening(self):
        threading.Thread(target=self.listen).start()

    def listen(self):
        while True:
            data = self.receive()
            if data['type'] == 'block':
                self.handle_block(data['block'])
            elif data['type'] == 'transaction':
                self.handle_transaction(data['transaction'])

    def handle_block(self, block):
        # TO DO: implement block validation and addition to blockchain
        print(f"Received block {block['hash']}")

    def handle_transaction(self, transaction):
        # TO DO: implement transaction validation and addition to transaction pool
        print(f"Received transaction {transaction['id']}")

class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def connect_nodes(self):
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                self.nodes[i].add_peer(self.nodes[j])
                self.nodes[j].add_peer(self.nodes[i])

    def start_network(self):
        for node in self.nodes:
            node.start_listening()
