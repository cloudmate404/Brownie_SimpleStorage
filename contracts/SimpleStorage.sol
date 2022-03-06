// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // THIS WILL GET INITIALIZED TO 0!!
    uint256 favoriteNumber;

    //THIS IS LIKE CREATING AN OBJECT
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    //THIS IS A DYNAMIC ARRAY(iT CAN INCREASE AND DECREASE)
    People[] public xyz;

    mapping(string => uint256) public nameToFavoriteNumber;

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        xyz.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }

    function retreive() public view returns (uint256) {
        return favoriteNumber;
    }

    // bool favoriteBool;
    // string favoriteString = "String";
    // int256 favoriteInt = -5;
    // address favoriteAddress = 0xb2Cff38e6130F2043fDaB93F9FE1b0718cB29bd2;
    // bytes32 favoriteBytes = "cat";
}
