import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class NeuroEconomicModel:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100)

    def train(self, data):
        self.model.fit(data.drop('target', axis=1), data['target'])

    def predict(self, data):
        return self.model.predict(data)
