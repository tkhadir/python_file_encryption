import os
from os import urandom
import threading
import blowfish

print("--------start-------------")

filename="./../out/out0"
iv=b"here put your iv"
file = open(filename, 'rb')
msg = file.read()
file.close()
cipher = blowfish.Cipher(b"here put your key")
result = b"".join(cipher.decrypt_cbc(msg, iv)).decode()
print("clear msg : " + result)


outfile = open("./../decrypted/msg", 'w')
outfile.write(result)
outfile.close()
print("-------end----------------")