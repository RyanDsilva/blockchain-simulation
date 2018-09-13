from block import Block
from transaction import Transaction


class BlockChain:
    def __init__(self, name, proofOfWork, reward):
        self.name = name
        self.PROOF_OF_WORK = proofOfWork
        self.pendingTransactions = []
        self.miningReward = reward
        self.blocks = [self.generateGenesisBlock()]

    def __repr__(self):
        return "<BlockChain Name:%s\tProof Of Work:%s\tReward:%s\nPending Transactions:%s\nBlocks:%s>" % (self.name, self.PROOF_OF_WORK, self.miningReward, self.pendingTransactions, self.blocks)

    def getLastestBlock(self):
        return self.blocks[len(self.blocks) - 1]

    def generateGenesisBlock(self):
        genesis = Block(Transaction(None, None, 0), None)
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

    def minePendingTransactions(self, address):
        latestHash = self.getLastestBlock().currentHash
        block = Block(self.pendingTransactions[:5], latestHash)
        block.mineBlock(self.PROOF_OF_WORK)
        self.blocks.append(block)
        self.pendingTransactions = [
            Transaction(address, None, self.miningReward)]

    def createTransaction(self, transaction):
        self.pendingTransactions.append(transaction)

    def getBalance(self, address):
        balance = 0
        for block in self.blocks:
            for transaction in block.transactions:
                if transaction.fromAddress == address:
                    balance -= transaction.amount
                elif transaction.toAddress == address:
                    balance += transaction.amount
                else:
                    continue
        return balance
