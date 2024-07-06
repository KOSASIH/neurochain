import unittest
import json

class TestNeuroChain(unittest.TestCase):
    def setUp(self):
        self.neurochain = NeuroChain()

    def test_create_block(self):
        block = self.neurochain.create_block()
        self.assertIsInstance(block, Block)

    def test_add_block(self):
        block = self.neurochain.create_block()
        self.neurochain.add_block(block)
        self.assertEqual(len(self.neurochain.get_blockchain()), 2)

    def test_create_transaction(self):
        sender = "sender"
        recipient = "recipient"
        amount = 10
        transaction = self.neurochain.create_transaction(sender, recipient, amount)
        self.assertIsInstance(transaction, Transaction)

    def test_add_transaction(self):
        sender = "sender"
        recipient = "recipient"
        amount = 10
        transaction = self.neurochain.create_transaction(sender, recipient, amount)
        self.neurochain.add_transaction(transaction)
        self.assertEqual(len(self.neurochain.get_transaction_pool()), 1)

    def test_validate_transaction(self):
        sender = "sender"
        recipient = "recipient"
        amount = 10
        transaction = self.neurochain.create_transaction(sender, recipient, amount)
        self.assertTrue(self.neurochain.validate_transaction(transaction))

    def test_mine(self):
        miner_address = "miner"
        miner = self.neurochain.get_miner(miner_address)
        miner.mine()
        self.assertEqual(len(self.neurochain.get_blockchain()), 2)

    def test_deploy_contract(self):
        contract_code = "contract_code"
        contract_address = "contract_address"
        contract = self.neurochain.deploy_contract(contract_code, contract_address)
        self.assertIsInstance(contract, SmartContract)

    def test_execute_contract(self):
        contract_code = "contract_code"
        contract_address = "contract_address"
        contract = self.neurochain.deploy_contract(contract_code, contract_address)
        input_data = "input_data"
        result = self.neurochain.execute_contract(contract_address, input_data)
        self.assertEqual(result, "Contract executed successfully")

if __name__ == '__main__':
    unittest.main()
