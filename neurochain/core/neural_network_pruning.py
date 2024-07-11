import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

class NeuralNetworkPruning(nn.Module):
    def __init__(self, model):
        super(NeuralNetworkPruning, self).__init__()
        self.model = model

    def l1_regularization(self, amount):
        # Apply L1 regularization to the model
        for module in self.model.modules():
            if isinstance(module, nn.Linear):
                module.weight.data.add_(-amount * torch.sign(module.weight.data))

    def l2_regularization(self, amount):
        # Apply L2 regularization to the model
        for module in self.model.modules():
            if isinstance(module, nn.Linear):
                module.weight.data.add_(-amount * module.weight.data)

    def magnitude_based_pruning(self, threshold):
        # Prune weights with small magnitudes
        for module in self.model.modules():
            if isinstance(module, nn.Linear):
                mask = torch.abs(module.weight.data) > threshold
                prune.custom_from_mask(module, name='weight', mask=mask)
