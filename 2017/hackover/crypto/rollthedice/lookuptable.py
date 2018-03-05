#!/usr/bin/env python3
from Crypto.Cipher import AES
import base64
import os
import binascii

EncodeAES = lambda c, s: c.encrypt(s)
DecodeAES = lambda c, e: c.decrypt(e)
BLOCK_SIZE=16

secret = '1111111111111111'

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
		
#save output of this file to table.txt
#python3 lookuptable.py > table.txt
