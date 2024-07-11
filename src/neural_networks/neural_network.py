import torch
import torch.nn as nn
import torch.optim as optim

class NeuralNetwork(nn.Module):
    def __init__(self, config):
        super(NeuralNetwork, self).__init__()
        self.config = config
        self.fc1 = nn.Linear(config['input_dim'], config['hidden_dim'])
        self.fc2 = nn.Linear(config['hidden_dim'], config['output_dim'])
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(config['dropout_rate'])

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

    def train(self, data, labels):
        criterion = nn.MSELoss()
        optimizer = optim.Adam(self.parameters(), lr=self.config['learning_rate'])
        for epoch in range(self.config['num_epochs']):
            optimizer.zero_grad()
            outputs = self.forward(data)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            print(f'Epoch {epoch+1}, Loss: {loss.item()}')

    def predict(self, data):
        return self.forward(data)
