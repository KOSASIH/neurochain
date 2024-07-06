import time
from neurochain import Block, Transaction

class Miner:
    def __init__(self, neurochain):
        self.neurochain = neurochain

    def mine(self):
        while True:
            block = self.create_block()
            self.neurochain.add_block(block)
            time.sleep(10)  # mine a new block every 10 seconds

    def create_block(self):
        transactions = self.neurochain.get_transaction_pool()
        block = Block(self.neurochain.get_latest_block().hash, transactions)
        return block

    def create_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        return transaction
