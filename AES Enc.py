from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
import time

#key = 'sixteen byte key'.encode("utf-8")
key = unhexlify('6F6D3A4F87F31E86CEADB19D8690353D8B92A16C13A575E23A61453020A32EB1'.encode("utf-8"))
dataEnc = '32'.encode("utf-8")


#iv = 'abcdefghijklmnop'.encode("utf-8")
iv = unhexlify('5BDF9E75B81998D15E0E58B77DA6F4D9'.encode("utf-8"))

encryptor = AES.new(key, AES.MODE_CBC, iv)
decryptor = AES.new(key,AES.MODE_CBC, iv)

dataEnc = pad(dataEnc,AES.block_size)
ciphertext = encryptor.encrypt(dataEnc)

print("Ciphertext : " + str(hexlify(ciphertext).decode("utf-8")))


plaintext = decryptor.decrypt(ciphertext)
plaintext = unpad(plaintext, AES.block_size)

print("Plaintext : " + str(plaintext.decode('utf-8')))