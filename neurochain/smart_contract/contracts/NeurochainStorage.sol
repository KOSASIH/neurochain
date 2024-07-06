// neurochain/smart_contract/contracts/NeurochainStorage.sol
pragma solidity ^0.8.0;

contract NeurochainStorage {
    mapping (address => uint256) public balances;

    function setBalance(address _address, uint256 _balance) public {
        balances[_address] = _balance;
    }

    function getBalance(address _address) public view returns (uint256) {
        return balances[_address];
    }
}
