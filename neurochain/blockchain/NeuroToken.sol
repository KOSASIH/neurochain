pragma solidity ^0.8.0;

contract NeuroToken {
    address private owner;
    mapping (address => uint256) public balances;

    constructor() public {
        owner = msg.sender;
    }

    function transfer(address recipient, uint256 amount) public {
        require(msg.sender == owner, "Only the owner can transfer tokens");
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
    }

    function getBalance(address account) public view returns (uint256) {
        return balances[account];
    }

    event Transfer(address indexed from, address indexed to, uint256 value);
}
