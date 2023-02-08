from web3 import Web3

ganache_url ="http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xc33E0184225206423efc648645a930c2dC52e97e"
account_2 = "0xBE2C486958b61c8e22e44C7dBBD641FE499D3B00"

privateKey = "ea55627306d53f1f4f0799b25e61ef44041a6b20ce5add27dd4e5743cbf8b39d"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
	
	'nonce': nonce,
	'to':  account_2,
	'value': web3.toWei(1,'ether'),
	'gas': 2000000,
	'gasPrice': web3.toWei('50','gwei')

}

signed_tx = web3.eth.account.signTransaction(tx,privateKey)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
