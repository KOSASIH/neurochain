import pandas as pd
from sklearn.ensemble import RandomForestClassifier

classCognitiveAnalytics:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self, data):
        self.model.fit(data.drop('target', axis=1), data['target'])

    def analyze(self, data):
        return self.model.predict(data)
