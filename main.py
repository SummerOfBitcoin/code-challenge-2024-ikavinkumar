import hashlib
import json
import os

# Define the difficulty target
DIFFICULTY_TARGET = "0000ffff00000000000000000000000000000000000000000000000000000000"

def calculate_hash(block_header):
    """
    Calculate the hash of the block header.
    """
    return hashlib.sha256(block_header.encode()).hexdigest()

def validate_transaction(transaction):
    """
    Validate a transaction based on specified criteria.
    """
    # Implement your transaction validation logic here
    # For simplicity, this function currently returns True for all transactions
    return True

def mine_block(transactions):
    """
    Mine a block with the given transactions.
    """
    block_header = "Example block header"  # Placeholder for the block header
    nonce = 0
    while True:
        # Update the block header with the nonce
        block_header_with_nonce = block_header + str(nonce)
        # Calculate the hash of the block header with nonce
        block_hash = calculate_hash(block_header_with_nonce)
        # Check if the hash meets the difficulty target
        if block_hash < DIFFICULTY_TARGET:
            break
        nonce += 1
    return block_header_with_nonce, nonce

def main():
    # List all JSON files in the mempool folder
    mempool_files = [file for file in os.listdir("mempool") if file.endswith(".json")]

    # Read transaction data from each JSON file in the mempool folder
    transactions = []
    for file_name in mempool_files:
        with open(os.path.join("mempool", file_name)) as file:
            file_transactions = json.load(file)
            # Assuming each file contains a list of transactions
            transactions.extend(file_transactions)

    # Validate transactions and filter out invalid ones
    valid_transactions = [tx for tx in transactions if validate_transaction(tx)]

    # Mine the block
    block_header, nonce = mine_block(valid_transactions)

    # Serialize the coinbase transaction (placeholder)
    coinbase_transaction = "Serialized coinbase transaction"

    # Write the mined transactions to output.txt
    with open("output.txt", "w") as output_file:
        output_file.write(block_header + "\n")
        output_file.write(coinbase_transaction + "\n")
        for tx in valid_transactions:
            # Ensure tx is a dictionary representing a transaction
            if isinstance(tx, dict) and "txid" in tx:
                output_file.write(tx["txid"] + "\n")
            else:
                print("Invalid transaction format:", tx)

if __name__ == "__main__":
    main()
