// neurochain/tests/Neurochain.test.js
const { expect } = require('chai');
const { deployments, getNamedAccounts } = require('hardhat');

describe('Neurochain', () => {
    let deployer, user;
    let neurochain;

    beforeEach(async () => {
        ({ deployer, user } = await getNamedAccounts());
        neurochain = await deployments.deploy('Neurochain', {
            from: deployer,
            args: [],
        });
    });

    it('should execute transaction correctly', async () => {
        const tx = await neurochain.executeTransaction({ from: user });
        expect(tx.receipt.status).to.equal(true);
    });
});
