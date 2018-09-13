import hashlib
from datetime import datetime as dt


class Transaction:
    def __init__(self, toAddress, fromAddress, amount):
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.amount = amount


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


class BlockChain:
    def __init__(self, name, proofOfWork):
        self.name = name
        self.PROOF_OF_WORK = proofOfWork
        self.blocks = [self.generateGenesisBlock()]

    def getLastestBlock(self):
        return self.blocks[len(self.blocks) - 1]

    def generateGenesisBlock(self):
        genesis = Block(Transaction('RYCOIN', 'RYCOIN', 0), None)
        genesis.mineBlock(self.PROOF_OF_WORK)
        return genesis

    def validateChain(self):
        for index, block in enumerate(self.blocks, start=1):
            prev = self.blocks[index - 1]
            if block.currentHash != block.calculateHash():
                return False
            if block.previousHash != prev.currentHash:
                return False
        return True

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLastestBlock().currentHash
        newBlock.mineBlock(self.PROOF_OF_WORK)
        self.blocks.append(newBlock)


RYCOIN = BlockChain('RYCOIN', '0000')
