from brownie import SimpleStorage, accounts


def test_deploy():
    # Test is separated into 3 categories
    # 1. Arrange
    account = accounts[0]
    # 2. Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retreive()
    expected = 0
    # 3. assert
    assert starting_value == expected


def test_update_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # 2. Act
    added_value = simple_storage.store(15, {"from": account})
    expected = 15
    assert expected == simple_storage.retreive()
