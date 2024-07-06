import requests
import json

class NeuroChainIoT:
    def __init__(self):
        self.api_url = "https://api.neurochain.io/iot"

    def send_data(self, device_id, data):
        headers = {"Content-Type": "application/json"}
        payload = {"device_id": device_id, "data": data}
        response = requests.post(self.api_url, headers=headers, json=payload)
        return response.json()

    def receive_data(self, device_id):
        headers = {"Content-Type": "application/json"}
        payload = {"device_id": device_id}
        response = requests.get(self.api_url, headers=headers, params=payload)
        return response.json()

iot = NeuroChainIoT()
device_id = "device123"
data = {"temperature": 25, "humidity": 60}
response = iot.send_data(device_id, data)
print(response)
