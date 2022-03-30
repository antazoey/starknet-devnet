#!/bin/bash

TEST_DIRECTORY=test/contracts
ARTIFACTS_DIRECTORY=test/artifacts

# delete all artifacts
rm -rf $ARTIFACTS_DIRECTORY

# create artifacts directory
mkdir -p $ARTIFACTS_DIRECTORY

echo "Compiling contracts with $(starknet-compile --version)"

# compile Cairo test contracts
for contract in "$TEST_DIRECTORY"/cairo/*.cairo; do
    echo "Compiling $contract"

    # create contract directory
    directory=$ARTIFACTS_DIRECTORY/contracts/cairo/"${contract##*/}"
    mkdir -p "$directory"


    basename=$(basename "$contract")
    output=$directory/"${basename%.*}.json"
    abi=$directory/"${basename%.*}_abi.json"

    starknet-compile --output "$output" --abi "$abi" "$contract"
done

# compile Solidity test contracts
npx hardhat compile

echo "Done"