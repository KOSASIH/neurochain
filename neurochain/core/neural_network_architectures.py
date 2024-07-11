import torch
import torch.nn as nn
import torch.nn.functional as F

class GraphNeuralNetwork(nn.Module):
    def __init__(self, num_layers, hidden_dim):
        super(GraphNeuralNetwork, self).__init__()
        self.num_layers = num_layers
        self.hidden_dim = hidden_dim
        self.layers = nn.ModuleList([self._create_layer() for _ in range(num_layers)])

    def _create_layer(self):
        return nn.Linear(self.hidden_dim, self.hidden_dim)

    def forward(self, x, adj):
        # Forward pass through the GNN
        for layer in self.layers:
            x = F.relu(layer(x))
            x = torch.bmm(adj, x)
        return x

class Transformer(nn.Module):
    def __init__(self,num_layers, hidden_dim):
        super(Transformer, self).__init__()
        self.num_layers = num_layers
        self.hidden_dim = hidden_dim
        self.layers = nn.ModuleList([self._create_layer() for _ in range(num_layers)])

    def _create_layer(self):
        return nn.TransformerEncoderLayer(self.hidden_dim, 8)

    def forward(self, x):
        # Forward pass through the Transformer
        for layer in self.layers:
            x = layer(x)
        return x

class ResidualNetwork(nn.Module):
    def __init__(self, num_layers, hidden_dim):
        super(ResidualNetwork, self).__init__()
        self.num_layers = num_layers
        self.hidden_dim = hidden_dim
        self.layers = nn.ModuleList([self._create_layer() for _ in range(num_layers)])

    def _create_layer(self):
        return nn.Sequential(
            nn.Linear(self.hidden_dim, self.hidden_dim),
            nn.ReLU(),
            nn.Linear(self.hidden_dim, self.hidden_dim)
        )

    def forward(self, x):
        # Forward pass through the ResNet
        for layer in self.layers:
            x = x + layer(x)
        return x
