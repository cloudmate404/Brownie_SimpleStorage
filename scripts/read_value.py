from brownie import SimpleStorage, accounts, config


def read_contract():
    # "Contract[-1]" gets us the most recent deployment
    simple_storage = SimpleStorage[-1]
    # go take the index thats one less than the length
    # ABI
    # Address
    print(simple_storage.retreive())


def main():
    read_contract()
