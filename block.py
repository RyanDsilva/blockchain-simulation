import hashlib
from datetime import datetime as dt


class Block:
    def __init__(self, transaction, previousHash):
        self.createdAt = dt.now()
        self.transaction = transaction
        self.nonce = 0
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()

    def calculateHash(self):
        hashString = str(self.createdAt) + str(self.nonce) + \
            str(self.transaction) + str(self.createdAt)
        hashString = hashString.encode()
        return hashlib.sha256(hashString).hexdigest()

    def mineBlock(self, PROOF_OF_WORK):
        while self.currentHash[:len(PROOF_OF_WORK)] != PROOF_OF_WORK:
            self.nonce += 1
            self.currentHash = self.calculateHash()
