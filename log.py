import time
from Crypto.Cipher import AES
from pykeyboard import PyKeyboard
from pymouse import PyMouse

fichier = open("hash", "r")

key = fichier.read()

fichier.close()
fichier = open("iv", "r")

iv = fichier.read()

fichier.close()
fichier = open("cipher", "r")

len = int(fichier.readline())
cipher = fichier.readline()

fichier.close()

aes = AES.new(key, AES.MODE_CBC, iv)

mp = aes.decrypt(cipher)[-len:]

k = PyKeyboard()
m = PyMouse()

time.sleep(1)
k.type_string(mp)
k.tap_key('return')
time.sleep(1)
m.move(500, 500)
time.sleep(1)
m.move(0, 0)
m.move(0, 0)