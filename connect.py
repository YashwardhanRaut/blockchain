from web3 import Web3
from web3.middleware import geth_poa_middleware
# from web3.middleware.geth_poa import geth_poa_middleware

from eth_account import Account

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Check connection
print(f"Connected to blockchain: {w3.isConnected()}")

# Add middleware for PoA networks
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Use your private key
private_key = "0xe97f4d3b645fbcaa17d018834d109c0f706b94a6d804488b20695a6af586e5b7"  # Replace with the private key
account = Account.from_key(private_key)
print(f"Using account: {account.address}")
