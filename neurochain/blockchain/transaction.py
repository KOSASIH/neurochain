import hashlib

class Transaction:
    def __init__(self, sender, recipient, amount, data):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the transaction hash using a cryptographic hash function
        pass
