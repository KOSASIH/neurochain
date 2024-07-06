import hashlib
import ecdsa
import os

class Wallet:
    def __init__(self):
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def generate_address(self):
        return hashlib.sha256(self.public_key.to_string()).hexdigest()

    def sign_transaction(self, transaction):
        signature = self.private_key.sign(transaction.encode())
        return signature

    def verify_signature(self, signature, transaction, public_key):
        verifying_key = ecdsa.VerifyingKey.from_string(public_key, curve=ecdsa.SECP256k1)
        return verifying_key.verify(signature, transaction.encode())

    def save_wallet(self, filename):
        with open(filename, 'w') as f:
            f.write(self.private_key.to_string().hex())

    @classmethod
    def load_wallet(cls, filename):
        with open(filename, 'r') as f:
            private_key = bytes.fromhex(f.read())
            wallet = cls()
            wallet.private_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
            wallet.public_key = wallet.private_key.get_verifying_key()
            return wallet
