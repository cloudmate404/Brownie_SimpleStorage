# Define we want to run this deploy
# def is how you define a function

# brownie has an account package that knows how to work with accounts, so we imp ort it
from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    # DIFFERENT METHODS OF ACCESSING ACCOUNTS

    # we want to take the account that appears at the zero index "account[0]"
    # account = accounts[0]

    # To get the account we added manually
    # account = accounts.load("freecodecamp-account")

    # To work with account info added to .env file
    # account = accounts.add(os.getenv("PRIVATE_KEY"))

    # To work with the brownie-config.yaml, add config to import brownie at the top
    # account = accounts.add(config["wallets"]["from_key"])

    # for now, we should just stick to ganache account
    account = get_account()
    # This will deploy the solidity contract and store it in the simple_storage value
    # Anytime you want to make a state change i.e a transaction, we need to add who we are transacting from "{"from":}"
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retreive()
    add_value = simple_storage.store(24, {"from": account})
    add_value.wait(1)
    updated_stored_value = simple_storage.retreive()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()


# 0x822A57502EE0480291A852206cA41ae8738795ef
