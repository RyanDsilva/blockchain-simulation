class Transaction:
    def __init__(self, toAddress, fromAddress, amount):
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.amount = amount

    def __repr__(self):
        return " <Transaction To:%s\tFrom:%s\tAmount:%s>" % (self.toAddress, self.fromAddress, self.amount)
