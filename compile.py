from solcx import install_solc
install_solc("0.8.0")  # Replace "0.8.0" with your Solidity version


from solcx import compile_standard
import json

# Load the Solidity contract
with open("MyToken.sol", "r") as file:
    contract_code = file.read()

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"MyToken.sol": {"content": contract_code}},
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    }
})

# Save the compiled code
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Extract ABI and bytecode
abi = compiled_sol["contracts"]["MyToken.sol"]["MyToken"]["abi"]
bytecode = compiled_sol["contracts"]["MyToken.sol"]["MyToken"]["evm"]["bytecode"]["object"]
