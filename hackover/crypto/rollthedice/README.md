#Hack0ver 2016 : rollthedice
solved by illustris, cryptator
##Challenge
```
The new cyber casinos are using high speed digital cyber dices to provide the best available gaming experience. Play a brand new dice game at new levels and win. Please note that you have to upgrade to blockchain 3.0 to receive your profits via a smart contract 2.0.

nc challenges.hackover.h4q.it 1415
```
[Source code](rollthedice.tar.xz) is given.
15 points

##Solution
The server sends an encrypted message of the format . The plaintext is of the format
>0000000dxxxxxxxxxxxxxxxxxxxxxxxx

where d is the number the server rolled, with value 1-6, and x is random. We are then required to send our own ciphertext. The server responds with its key, and expects us to respond with our key. Server then decrypts our message and checks if it is the number opposite to the one the server rolled.

The solution is to make a ciphertext and a set of keys such that the ciphertext can be decrypted into any plaintext of the format 0000000dxxxxxxxx by sending the corresponding key. We wrote [this script](lookuptable.py) to generate [a list of keys](table.txt). Then [this script](rollthedice.py) was used to get the number from the server and respond with the corresponding key.