import torch
import torch.nn as nn
import torch.optim as optim

class NeuroChainOptimizer(optim.Optimizer):
    def __init__(self, params, lr=0.001, betas=(0.9, 0.999), eps=1e-8):
        # Initialize the optimizer with meta-learning capabilities
        self.meta_lr = 0.01
        self.meta_betas = (0.9, 0.999)
        self.meta_eps = 1e-8
        super(NeuroChainOptimizer, self).__init__(params, lr, betas, eps)

    def step(self, closure=None):
        # Perform a step of the optimizer with gradient regularization
        loss = closure()
        self.zero_grad()
        loss.backward()
        self._regularize_gradients()
        self._update_params()

    def _regularize_gradients(self):
        # Regularize gradients to prevent exploding gradients
        for group in self.param_groups:
            for p in group['params']:
                p.grad.data.add_(p.data, alpha=self.meta_lr)

    def _update_params(self):
        # Update parameters with automatic learning rate scheduling
        for group in self.param_groups:
            for p in group['params']:
                p.data.add_(p.grad.data, alpha=-group['lr'])
                group['lr'] *= 0.99  # decay learning rate
