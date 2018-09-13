import hashlib
from datetime import datetime as dt


class Transaction:
    def __init__(self, toAddress, fromAddress, amount):
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.amount = amount


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


class BlockChain:
    def __init__(self, name, proofOfWork):
        self.name = name
        self.blocks = []
        self.PROOF_OF_WORK = proofOfWork

    def getLastestBlock(self):
        return self.blocks[len(self.blocks) - 1]

    def generateGenesisBlock(self):
        pass

    def validateChain(self):
        pass

    def addBlock(self):
        pass

    def proofOfWork(self):
        pass
