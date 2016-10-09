#!/usr/bin/python2
from pwn import *
from Crypto.Cipher import AES
import base64
import os
import binascii

BLOCK_SIZE = 16
tube = remote('challenges.hackover.h4q.it', 1415, level=logging.ERROR)

EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))

tube.recvuntil('Win 32 consecutive rounds and I will give you a flag.\n\n')

while(True):
	print count
	response1 = tube.recvline().strip()
	print response1
	roll1=response1.split()
	# print roll1[3]

	tube.sendafter("Your dice roll: ",base64.b64encode("1111111111111111"))
	tube.send("\n")
	response2 = tube.recvline().strip()
	print response2
	key1=response2.split()
	# print key1[2]
	key_server=base64.b64decode(key1[2])
	cipher_server=AES.new(key_server)

	decode_server = DecodeAES(cipher_server, roll1[3])
	first2=decode_server[:2]

	if first2=='\x00\x01':
		our_key=base64.b64encode(binascii.unhexlify('feaa4504f380c37ecfa7041d14b39845'))
		tube.sendafter("Your key: ",our_key)
		tube.send("\n")

	elif first2=='\x00\x02':
		our_key=base64.b64encode(binascii.unhexlify('fc61a307c5ea9143aa58f4cadac12112'))
		tube.sendafter("Your key: ",our_key)
		tube.send("\n")

	elif first2=='\x00\x03':
		our_key=base64.b64encode(binascii.unhexlify('a2753579eaaed9c33b78903c050af74f'))
		tube.sendafter("Your key: ",our_key)
		tube.send("\n")


	elif first2=='\x00\x04':
		our_key=base64.b64encode(binascii.unhexlify('387c26120ea75ffcf6fd53ca0e9f307d'))
		tube.sendafter("Your key: ",our_key)
		tube.send("\n")

	elif first2=='\x00\x05':
		our_key=base64.b64encode(binascii.unhexlify('0ff4b835e7bf84f849560dbd45043b9d'))
		tube.sendafter("Your key: ",our_key)
		tube.send("\n")

	elif first2=='\x00\x06':
		our_key=base64.b64encode(binascii.unhexlify('abed678e6f5024b4291840d0afa68814'))
		tube.sendafter("Your key: ",our_key)
		tube.send("\n")

