#!/bin/bash

# Execute the Python script
python main.py

# Print the block header from the output
echo "Block Header:"
head -n 1 output.txt

# Print the serialized coinbase transaction from the output
echo "Serialized Coinbase Transaction:"
sed -n '2p' output.txt

# Print the transaction IDs (txids) of the transactions mined in the block, in order
echo "Transaction IDs (txids):"
tail -n +3 output.txt
