import pandas as pd
import numpy as np
import networkx as nx
from sklearn.ensemble import IsolationForest

class BlockchainDataAnalytics:
    def __init__(self, data):
        self.data = data

    def time_series_analysis(self):
        # Perform time-series analysis on blockchain data
        ts_data = self.data.resample('1h').mean()
        ts_data_diff = ts_data.diff().dropna()
        acf = ts_data_diff.autocorrelation()
        pacf = ts_data_diff.partial_autocorrelation()
        return acf, pacf

    def graph_analysis(self):
        # Perform graph analysis on blockchain data
        G = nx.Graph()
        for tx in self.data:
            G.add_node(tx['tx_id'])
            for input_tx in tx['inputs']:
                G.add_edge(input_tx, tx['tx_id'])
        degree_centrality = nx.degree_centrality(G)
        betweenness_centrality = nx.betweenness_centrality(G)
        return degree_centrality, betweenness_centrality

    def anomaly_detection(self):
        # Perform machine learning-based anomaly detection on blockchain data
        X = self.data.drop(['tx_id', 'timestamp'], axis=1)
        if = IsolationForest(contamination=0.1)
        if.fit(X)
        anomalies = if.predict(X)
        return anomalies
