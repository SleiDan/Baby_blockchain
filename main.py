from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Hash.SHA512


class KeyPair:
    def genKeyPair(self):
        privateKey = RSA.generate(2048)
        publicKey = privateKey.publickey()
        self.privateKey = privateKey.exportKey(format='PEM')
        self.publicKey = publicKey.exportKey(format='PEM')
        return self.publicKey, self.privateKey

    def __init__(self):
        self.publicKey, self.privateKey = self.genKeyPair()

    def printKeyPair(self):
        print(self.publicKey)
        print(self.privateKey)

    def __str__(self):
        return str(self.publicKey) + " " + str(self.privateKey)


class Signature:
    def signData(self, txt, key, hashAlg = Crypto.Hash.SHA512):
        signature = PKCS1_v1_5.new(RSA.importKey(key))
        hash = hashAlg.new(txt)
        return signature.sign(hash)

    def verifySignature(self, sign, txt, key, hashAlg = Crypto.Hash.SHA512):
        hash = hashAlg.new(txt)
        verif = PKCS1_v1_5.new(RSA.importKey(key))
        return verif.verify(hash, sign)


class Account:
    def __init__(self):
        self.genAccount()

    def genAccount(self):
        kPair1 = KeyPair()
        self.wallet = []
        self.wallet.append(kPair1.genKeyPair())
        self.accountID = self.wallet[0]
        return self.wallet, self.accountID

    def addKeyPairToWallet(self):
        self.wallet.append(D.genKeyPair())

    def signData(self,text, index):
        key = self.wallet[index][1]
        Sign1 = Signature()
        return Sign1.signData(text, key)
    
class Operation:
    def __init__(self,sender, reciever, amount, signature):
        self.sender, self.reciever, self.amount, self.signature = self.createOperation(sender, reciever, amount, signature)

    def createOperation(self,sender, reciever, amount, signature):
        self.sender = sender
        self.reciever = reciever
        self.amount = str(amount)
        self.signature = signature
        return self.sender, self.reciever, self.amount, self.signature

    def verifyOperation(self, sender, signature, amount):
        Sign2 = Signature()
        return Sign2.verifySignature(signature,amount.encode(),sender)

class Transaction:
    def __init__(self, transactionID, setOfOperations, nonce):
        self.transactionID = transactionID
        self.setOfOperetions = setOfOperations
        self.nonce = nonce

    def createTransaction(self, setOfOperations, nonce):
        t = ''
        self.setOfOperetions = setOfOperations
        self.nonce = nonce
        self.transactionID = Crypto.Hash.SHA512.new(t.join(setOfOperations) + nonce)
        return self


Sign = Signature()
kPair = KeyPair()
Acc = Account()
privateKey = RSA.generate(2048)
publicKey = privateKey.publickey()
privateKey = privateKey.exportKey(format='PEM')
publicKey = publicKey.exportKey(format='PEM')
kPair.genKeyPair()
kPair.printKeyPair()
Acc.genAccount()
print('Введите месседж:')
message = input()
sign = Acc.signData(message.encode(), 0)
result = Sign.verifySignature(sign, message.encode(), Acc.wallet[0][0])
print(result)
