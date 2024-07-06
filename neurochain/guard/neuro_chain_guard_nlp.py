import torch
import torch.nn as nn
from neuro_chain_hub import NeuroChainGuardNLP

class NeuroChainGuardNLPModel(nn.Module):
    def __init__(self):
        super(NeuroChainGuardNLPModel, self).__init__()
        self.embedding = nn.Embedding(10000, 128)
        self.lstm = nn.LSTM(128, 128, num_layers=2, batch_first=True)
        self.fc = nn.Linear(128, 10)

    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm(x)
        x = self.fc(x[:, -1, :])
        return x

model = NeuroChainGuardNLPModel()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Load data
data = NeuroChainGuardNLP.load_data("nlp_data.csv")

# Train model
for epoch in range(10):
    for x, y in data:
        x = torch.tensor(x)
        y = torch.tensor(y)
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Evaluate model
model.eval()
test_data = NeuroChainGuardNLP.load_data("test_data.csv")
test_loss = 0
correct = 0
with torch.no_grad():
    for x, y in test_data:
        x = torch.tensor(x)
        y = torch.tensor(y)
        output = model(x)
        loss = criterion(output, y)
        test_loss += loss.item()
        _, predicted = torch.max(output, 1)
        correct += (predicted == y).sum().item()

accuracy = correct / len(test_data)
print(f"Test Loss: {test_loss / len(test_data)}")
print(f"Test Accuracy: {accuracy:.2f}%")
