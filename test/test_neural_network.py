import unittest
from src.neural_networks.neural_network import NeuralNetwork

class TestNeuralNetwork(unittest.TestCase):
    def test_neural_network(self):
        neural_network = NeuralNetwork()
        self.assertIsNotNone(neural_network)
