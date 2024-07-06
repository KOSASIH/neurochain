// neurochain/smart_contract/contracts/Neurochain.sol
pragma solidity ^0.8.0;

import "./NeurochainStorage.sol";
import "./NeurochainLogic.sol";

contract Neurochain {
    NeurochainStorage private storage;
    NeurochainLogic private logic;

    constructor() {
        storage = new NeurochainStorage();
        logic = new NeurochainLogic();
    }

    function executeTransaction() public {
        logic.executeTransaction(storage);
    }
}
