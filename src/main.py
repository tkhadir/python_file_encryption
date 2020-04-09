import os
from os import urandom
import threading
import blowfish

content = []
output = []

class Reader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        files = os.listdir('./../in/')
        for f in files:
            inFile = open('./../in/' + f, 'r')
            content.append(inFile.read())
            inFile.close()

class Writer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        count = 0
        for o in output:
            outFile = open('./../out/out' + str(count), 'wb')
            outFile.write(o)
            outFile.close()
            count+=1

def getMsgToEncrypt(msg):
    msgToEncrypt = msg
    if len(msgToEncrypt) % 8 != 0:
        toAdd = 8 - len(msgToEncrypt) % 8
        count = 0
        while (count < toAdd):
            msgToEncrypt+="*"
            count+=1
    return msgToEncrypt.encode()

def encrypt(msg):
    iv = urandom(8)
    cipher = blowfish.Cipher(b"here put your key")
    result = b"".join(cipher.encrypt_cbc(getMsgToEncrypt(msg), iv))
    print("iv="+ str(iv))
    return result

print("debut de traitement")
thr = Reader()
thr.start()
thr.join()
print("fin de lecture")

print("debut de cryptage")
for c in content:
    output.append(encrypt(c))
print("fin de cryptage")

thw = Writer()
thw.start()
thw.join()
print("fin d'ecriture")

print("fin de traitement")




