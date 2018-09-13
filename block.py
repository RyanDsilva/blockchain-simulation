import hashlib
from datetime import datetime as dt


class Block:
    def __init__(self, transactions, previousHash):
        self.createdAt = dt.now()
        self.transactions = transactions
        self.nonce = 0
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()

    def __repr__(self):
        return "\n<Block Created At:%s\nTransaction:%s\nNonce:%s\tPrevious Hash:%s\nCurrent Hash:%s>\n" % (self.createdAt, self.transactions, self.nonce, self.previousHash, self.currentHash)

    def calculateHash(self):
        hashString = str(self.createdAt) + str(self.nonce) + \
            str(self.transactions) + str(self.createdAt)
        hashString = hashString.encode()
        return hashlib.sha256(hashString).hexdigest()

    def mineBlock(self, PROOF_OF_WORK):
        while self.currentHash[:len(PROOF_OF_WORK)] != PROOF_OF_WORK:
            self.nonce += 1
            self.currentHash = self.calculateHash()
