from block import Block
from transaction import Transaction


class BlockChain:
    def __init__(self, name, proofOfWork, reward):
        self.name = name
        self.PROOF_OF_WORK = proofOfWork
        self.pendingTransactions = []
        self.miningReward = reward
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
