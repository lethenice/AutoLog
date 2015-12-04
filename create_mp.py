#!/usr/bin/python
from sys import stdin
import getpass
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

print "Password needs to be <= 16"
mp = getpass.getpass()
mp2 = getpass.getpass()

if (mp != mp2) :
	sys.exit("Bad Password")

len = len(mp)

hash_f = open("hash", "w")
iv_f = open("iv", "w")
cipher_f = open("cipher", "w")

cipher_f.write(str(len))
cipher_f.write("\n")

sha = SHA256.new()
sha.update(mp)
hash = sha.digest()[:16]
iv = sha.digest()[-16:]
hash_f.write(hash)
iv_f.write(iv)

aes = AES.new(hash, AES.MODE_CBC, iv)
cipher_f.write(aes.encrypt('{:>16}'.format(mp)))

hash_f.close()
iv_f.close()
cipher_f.close()