import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []
        for i in range(len(layers) - 1):
            self.weights.append(np.random.rand(layers[i], layers[i + 1]))
            self.biases.append(np.random.rand(1, layers[i + 1]))

    def feedforward(self, x):
        for i in range(len(self.layers) - 1):
            x = np.dot(x, self.weights[i]) + self.biases[i]
            x = self.sigmoid(x)
        return x

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

nn = NeuralNetwork([784, 256, 10])
