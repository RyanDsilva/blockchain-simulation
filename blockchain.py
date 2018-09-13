import hashlib
from datetime import datetime as dt


class Block:
    def __init__(self, transaction, nonce, previousHash):
        self.createdAt = dt.now()
        self.transaction = transaction
        self.nonce = nonce
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()

    def calculateHash(self):
        hashString = str(self.createdAt) + str(self.nonce) + \
            str(self.transaction) + str(self.createdAt)
        hashString = hashString.encode()
        return hashlib.sha256(hashString).hexdigest()
