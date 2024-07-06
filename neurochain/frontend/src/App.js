// neurochain/frontend/src/App.js
import React, { useState, useEffect } from 'eact';
import Web3 from 'web3';

const App = () => {
    const [account, setAccount] = useState('');
    const [balance, setBalance] = useState(0);

    useEffect(() => {
        const web3 = new Web3(window.ethereum);
        const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

        contract.methods.getBalance(account).call()
           .then(balance => setBalance(balance));
    }, [account]);

    const handleTransaction = () => {
        const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
        contract.methods.executeTransaction().send({ from: account });
    };

    return (
        <div>
            <h1>Neurochain Frontend</h1>
            <p>Account: {account}</p>
            <p>Balance: {balance}</p>
            <button onClick={handleTransaction}>Execute Transaction</button>
        </div>
    );
};
