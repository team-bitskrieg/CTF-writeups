#TUCTF 2016 : Secure Transmission

##Challenge
[A PCAP file](files/40bec2fdb682af3046465a54f7776c8adb26ea4d.pcapng) is given. It is mentioned that the flag is in the form "flag{...}"
150 points

##Solution
Filtering with 
>tcp.stream eq 0

shows that [a .pyc file](files/client.pyc) was downloaded from 192.168.188.129 by 192.168.188.130. This file was decompiled using [Uncompyle2](https://github.com/wibiti/uncompyle2). The output is this:


```python
import socket
from Crypto import Random
rand = Random.new()
from Crypto.Cipher import AES
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.188.129', 54321))
welcome = s.recv(1024).strip('\n')
print welcome
g = s.recv(1024).strip('\n').split('g:')[1]
print g
p = s.recv(1024).strip('\n').split('p:')[1]
print p
A = s.recv(1024).strip('\n').split('A:')[1]
print A
prompt = s.recv(1024).strip('\n')
print prompt
A = int(A)
g = int(g)
p = int(p)
b = int(rand.read(8).encode('hex'), 16)
B = pow(g, b, p)
s.send(str(B))
my_key = pow(A, b, p)
print 'secret key: {}'.format(my_key)
msg = s.recv(1024).strip('\n')
print '********************'
print 'encrypted message:'
print msg.encode('hex')
print ''
plain = ''
for i in msg.split('\n'):
    if not i.startswith('Good data!'):
        aes_key = hex(my_key).strip('0x').strip('L')
        while len(aes_key) < 32:
            aes_key = '0' + aes_key

        obj = AES.new(aes_key.decode('hex'), AES.MODE_CBC, '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        plain += obj.decrypt(i)

print plain
```

b is randomly generated, and is used to generate the encryption key for AES encryption. The value of A,g,p,B can be found in 
>tcp.stream eq 1

We know B, which is pow(g, b, p). b can be found as the discrete log of B to the base g modulo p. This can be done in [bdcalc](http://www.di-mgt.com.au/bdcalc.html). 

```
> x=123114413580763739;g=429072158523821662;p=594830787528835483  # INPUT
> b=1;for k in (1..p) do b=modmul(b,g,p);breakif(b==x) done;
  println("The discrete log of ",x," to the base ",g," mod ",p," is ", k)
The discrete log of 123114413580763739 to the base 429072158523821662 mod 594830787528835483 is 747027
```

Once I had all the values, I modified the python code to solve the message extracted from the pcapng

```python
from Crypto import Random
from Crypto.Cipher import AES

g=429072158523821662
p=594830787528835483
A=313868463457946531
B=123114413580763739

print pow(g,747027,p)
b=747027

msg_hex="476f6f642064617461210a09f5d9d2c41db04aee983854244cc3435a6daa90d3e186b509c3ac9d4a94dc440a"
msg=msg_hex.decode('hex')
print 'encrypted message:'
print msg.encode('hex')
msg=msg.strip('\n')

plain = ''
my_key = pow(A, b, p)
for i in msg.split('\n'):
    if not i.startswith('Good data!'):
            aes_key = hex(my_key).strip('0x').strip('L')
            while len(aes_key) < 32:
                    aes_key = '0' + aes_key
            obj=AES.new(aes_key.decode('hex'),AES.MODE_CBC,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            plain += obj.decrypt(i)

print plain
```

which gives the flag
>flag{breaking_dh_like_the_nsa!} 