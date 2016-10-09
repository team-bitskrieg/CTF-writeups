#!/usr/bin/env python3
from Crypto.Cipher import AES
import base64
import os
import binascii

EncodeAES = lambda c, s: c.encrypt(s)
DecodeAES = lambda c, e: c.decrypt(e)
BLOCK_SIZE=16

secret = '1111111111111111'
'''
# cipher = AES.new(secret)
# key=format(i, 'x')
key = hex(i)
by = key

# by = bytes(i, "utf-8")
by ='0x' +str('0' * (18 - len(by)))+by[2:]
# b"abcde".decode("utf-8") 
# print(by)
'''
while(True):
	key=os.urandom(BLOCK_SIZE)
	cipher = AES.new(key)
	bytearray.fromhex(secret)
	decodeforkey=DecodeAES(cipher, secret)
	first2=decodeforkey[:2]
	if first2==b'\x00\x01':
		print(1)
		print(binascii.hexlify(key))
	elif first2==b'\x00\x02':
		print(2)
		print(binascii.hexlify(key))
	elif first2==b'\x00\x03':
		print(3)
		print(binascii.hexlify(key))

	elif first2==b'\x00\x04':
		print(4)
		print(binascii.hexlify(key))
	elif first2==b'\x00\x05':
		print(5)
		print(binascii.hexlify(key))
	elif first2==b'\x00\x06':
		print(6)
		print(binascii.hexlify(key))

	# print(binascii.hexlify(key))

# tube.recvuntil('Your key: ')
# response2 = tube.recvline()
# cipher_us = AES.new(secret)

# decoded = DecodeAES(cipher, roll1[3])

# encoded = EncodeAES(cipher, 'password')


# print 'Encrypted string:', encoded

# print 'Decrypted string:', decoded


