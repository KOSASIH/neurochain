import hashlib
import ecdsa

class Wallet:
    def __init__(self):
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def generate_address(self):
        return hashlib.sha256(self.public_key.to_string()).hexdigest()
