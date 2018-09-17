from flask import Flask, jsonify
from flask_cors import CORS

# Blockchain Files
from blockchain import BlockChain
from block import Block
from transaction import Transaction
from user import User

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


def init():
    RYCOIN = BlockChain('RYCOIN', '0000', 100)
    users = [
        User('Ryan', '127.0.0.1')
    ]
    return RYCOIN, users


@app.route('/blockchain')
def blockchain():
    pass


@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    pass


@app.route('/mine', methods=['GET', 'POST'])
def mine():
    pass


@app.route('/user', methods=['GET', 'POST'])
def users():
    pass


if __name__ == '__main__':
    app.run(debug=True)
