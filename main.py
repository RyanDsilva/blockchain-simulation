from blockchain import BlockChain
from user import User
from transaction import Transaction

BLOCKCHAIN_NAME = input('Enter the name of the BlockChain / CryptoCurrency\n')
PROOF_OF_WORK = input('Enter the Proof of Work (Hex Value Accepted)\n')
REWARD = int(input('Enter the Mining Reward\n'))


RYCOIN = BlockChain(BLOCKCHAIN_NAME, PROOF_OF_WORK, REWARD)
users = []

while True:
    main_choice = int(input(
        'Select An Option:\n1. Create User\t2. Mine Block\t3. Get Balance\t4. Create Transaction\t5. Exit\n'))
    if main_choice == 1:
        name = input('Enter Name:\n')
        address = input('Enter Address (Numeric):\n')
        newUser = User(name, address)
        users.append(newUser)
        print('User Created Successfully!')
    elif main_choice == 2:
        address = input('Enter Your Address:\n')
        for user in users:
            if address == user.address:
                RYCOIN.minePendingTransactions(user.address)
                print('Block Mined Successfully!')
    elif main_choice == 3:
        address = input('Enter Your Address:\n')
        for user in users:
            if address == user.address:
                bal = RYCOIN.getBalance(user.address)
                print('Your Balance is: ' + str(bal))
    elif main_choice == 4:
        toAdd = input('Enter Reciever\'s Address:\n')
        fAdd = input('Enter Your Address:\n')
        amount = int(input('Enter Amount\n'))
        newTransaction = Transaction(toAdd, fAdd, amount)
        RYCOIN.createTransaction(newTransaction)
        print('Transaction Made Successfully!')
    elif main_choice == 5:
        print(RYCOIN)
        exit()
