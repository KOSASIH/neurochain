import Web3 from 'web3';

class NeuroChainWallet {
    constructor() {
        this.web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.neurochain.io'));
    }

    async getBalance(address) {
        return this.web3.eth.getBalance(address);
    }

    async sendTransaction(from, to, amount) {
        return this.web3.eth.sendTransaction({
            from: from,
            to: to,
            value: amount,
            gas: '20000',
            gasPrice: '20.0'
        });
    }
}

export default NeuroChainWallet;
