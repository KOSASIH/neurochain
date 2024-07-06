import tensorflow as tf
from tensorflow import keras
from neuro_chain_hub import NeuroChainXAI

class NeuroChainXAIModel(keras.Model):
    def __init__(self):
        super(NeuroChainXAIModel, self).__init__()
        self.fc1 = keras.layers.Dense(128, activation='relu')
        self.fc2 = keras.layers.Dense(10)

    def call(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x

model = NeuroChainXAIModel()
xai = NeuroChainXAI(model)
xai.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
xai.fit(X_train, y_train, epochs=10)
