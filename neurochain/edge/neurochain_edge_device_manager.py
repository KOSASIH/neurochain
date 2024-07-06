import paho.mqtt.client as mqtt

class NeuroChainEdgeDeviceManager:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect('localhost', 1883)

    def publish(self, topic, message):
        self.client.publish(topic, message)

    def subscribe(self, topic):
        self.client.subscribe(topic)

manager = NeuroChainEdgeDeviceManager()
manager.publish('neurochain/edge/device', 'Hello, World!')
manager.subscribe('neurochain/edge/device')
