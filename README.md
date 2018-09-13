# Blockchain Simulation (RYCOIN)

### Simulation of A BlockChain in the Python Programming Language

## Features:

[1. SHA-256 Hashing](#sha-256)

[2. Proof Of Work](#proof-of-work)

[3. Mining Rewards](#mining-rewards)

---

## Implemenation:

### SHA-256

- Using Python's in-built `hashlib` library to hash the blocks with SHA-256 <br>

```python
# Creating the String
  hashString = str(nonce) + str(transaction) + ..
# Converting to Bytes
  hashString = hashString.encode()
# Hashing
  currentHash = hashlib.sha256(hashString)
```

### Proof Of Work

- Proof Of Work is a concept that allows the blockchain not to be spammed by thousands of pending blocks every second.
- It sets a requirement that the hash generated has to be in a specific format
- For example, hash should start with 0000
- In this example you can set the `PROOF_OF_WORK` value

```python
#Checking whether the first characters of hash are equal to the proof of work
while currentHash[:len(PROOF_OF_WORK)] != PROOF_OF_WORK:
    #Update Nonce
    nonce += 1
    #Re-calculate Hash
    currentHash = calculateHash()
```

- Since the hash cannot be changed without changing any value in the block, a `nonce` value is added that can be modified to calculate hash according to requirements.

### Mining Rewards

- Because of this proof of work concept, it takes resources to `mine` blocks and hence miners need to be rewarded for this in order to add blocks at a constant rate and help maintain the blockchain.
- The mining reward is pre-defined value for that specific block.

```python
# After the block is mined, pending transactions is set to have just the reward transaction
def minePendingTransactions(address):
    ......
    block.mineBlock(PROOF_OF_WORK)
    # Adding to chain
    blocks.append(block)
    # Reward Transaction
    pendingTransactions = [Transaction(address, None, miningReward)]
```

---

## References:

[Savjee Coin](https://github.com/SavjeeTutorials/SavjeeCoin)

> &copy; 2018 Ryan Dsilva
