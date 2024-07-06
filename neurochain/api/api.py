import json
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Welcome to NeuroChain API"

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    blockchain = neurochain.get_blockchain()
    return json.dumps(blockchain)

@app.route('/blockchain/<int:block_index>', methods=['GET'])
def get_block(block_index):
    block = neurochain.get_block(block_index)
    return json.dumps(block)

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = json.loads(flask.request.data)
    sender = data['sender']
    recipient = data['recipient']
    amount = data['amount']
    transaction = neurochain.create_transaction(sender, recipient, amount)
    neurochain.add_transaction(transaction)
    return json.dumps({'transaction_id': transaction.id})

@app.route('/mine', methods=['POST'])
def mine():
    data = json.loads(flask.request.data)
    miner_address = data['miner_address']
    miner = neurochain.get_miner(miner_address)
    miner.mine()
    return json.dumps({'block_hash': neurochain.get_latest_block().hash})

@app.route('/smart_contract', methods=['POST'])
def deploy_contract():
    data = json.loads(flask.request.data)
    contract_code = data['contract_code']
    contract_address = data['contract_address']
    contract = neurochain.deploy_contract(contract_code, contract_address)
    return json.dumps({'contract_address': contract_address})

@app.route('/smart_contract/<string:contract_address>', methods=['POST'])
def execute_contract(contract_address):
    data = json.loads(flask.request.data)
    input_data = data['input_data']
    contract = neurochain.get_contract(contract_address)
    result = contract.execute(input_data)
    return json.dumps({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
