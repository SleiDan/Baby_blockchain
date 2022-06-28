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
