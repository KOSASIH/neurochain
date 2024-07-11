import unittest
from src.quantum_resistant_cryptography.quantum_resistant_cryptography import QuantumResistantCryptography

class TestQuantumResistantCryptography(unittest.TestCase):
    def test_quantum_resistant_cryptography(self):
        quantum_resistant_cryptography = QuantumResistantCryptography()
        self.assertIsNotNone(quantum_resistant_cryptography)
