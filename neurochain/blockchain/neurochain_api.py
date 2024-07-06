from flask import Flask, request, jsonify
from neurochain_api import NeuroChainAPI

app = Flask(__name__)

api = NeuroChainAPI()

@app.route('/get_balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    balance = api.get_balance(address)
    return jsonify({'balance': balance})

@app.route('/send_transaction', methods=['POST'])
def send_transaction():
    from_address = request.form['from']
    to_address = request.form['to']
    amount = int(request.form['amount'])
    tx_hash = api.send_transaction(from_address, to_address, amount)
    return jsonify({'tx_hash': tx_hash})

if __name__ == '__main__':
    app.run(debug=True)
