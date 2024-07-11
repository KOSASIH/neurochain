import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralNetworkGraphNeuralNetworks:
    def __init__(self, model, graph):
        self.model = model
        self.graph = graph

    def graph_convolutional_networks(self):
        # Learn node representations using GCNs
        node_features = self.graph.node_features
        adjacency_matrix = self.graph.adjacency_matrix
        node_representations = self.model(node_features, adjacency_matrix)
        return node_representations

    def graph_attention_networks(self):
        # Learn node representations using GATs
        node_features = self.graph.node_features
        adjacency_matrix = self.graph.adjacency_matrix
        node_representations = self.model(node_features, adjacency_matrix)
        return node_representations

    def graph_autoencoders(self):
        # Learn node representations using GAEs
        node_features = self.graph.node_features
        adjacency_matrix = self.graph.adjacency_matrix
        node_representations = self.model(node_features, adjacency_matrix)
        return node_representations
