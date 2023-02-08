from web3 import Web3

infura_url = "https://celo-mainnet.infura.io/v3/2b41ea1352e4487eb071bf3c80a26fd6"
web3 =Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

#la información de abajo de la devuelve de forma precisa en una terminal tal com CMD
balance = web3.eth.getBalance("0xcF6BB5389c92Bdda8a3747Ddb454cB7a64626C63")
print(web3.fromWei(balance, 'ether'))
print(balance)
