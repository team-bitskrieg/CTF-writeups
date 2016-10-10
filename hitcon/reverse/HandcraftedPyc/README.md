#hitcon 2016 : Handcrafted Pyc
Solved by codelec and illustris
##Challenge
```
Can your brain be a Python VM? (Please use Python 2.7)

```
[crackme.py](crackme.py)

##Solution
The py file is running python bytecode using marshal.load. The bytecode itself can be extracted by

```python
>>> import zlib
>>> import base64
>>> d=zlib.decompress(base64.b64decode('eJyNVktv00AQXm/eL0igiaFA01IO4cIVCUGFBBJwqRAckLhEIQmtRfPwI0QIeio/hRO/hJ/CiStH2M/prj07diGRP43Hs9+MZ2fWMxbnP6mux+oK9xVMHPFViLdCTB0xkeKDFEFfTIU4E8KZq8dCvB4UlN3hGEsdddXU9QTLv1eFiGKGM4cKUgsFCNLFH7dFrS9poayFYmIZm1b0gyqxMOwJaU3r6xs9sW1ooakXuRv+un7Q0sIlLVzOCZq/XtsK2oTSYaZlStogXi1HV0iazoN2CV2HZeXqRQ54TlJRb7FUlKyUatISsdzo+P7UU1Gb1POdMruckepGwk9tIXQTftz2yBaT5JQovWvpSa6poJPuqgao+b9l5Aj/R+mLQIP4f6Q8Vb3g/5TB/TJxWGdZr9EQrmn99fwKtTvAZGU7wzS7GNpZpDm2JgCrr8wrmPoo54UqGampFIeS9ojXjc4E2yI06bq/4DRoUAc0nVnng4k6p7Ks0+j/S8z9V+NZ5dhmrJUM/y7JTJeRtnJ2TSYJvsFq3CQt/vnfqmQXt5KlpuRcIvDAmhnn2E0t9BJ3SvB/SfLWhuOWNiNVZ+h28g4wlwUp00w95si43rZ3r6+fUIEdgOZbQAsyFRRvBR6dla8KCzRdslar7WS+a5HFb39peIAmG7uZTHVm17Czxju4m6bayz8e7J40DzqM0jr0bmv9PmPvk6y5z57HU8wdTDHeiUJvBMAM4+0CpoAZ4BPgJeAYEAHmgAUgAHiAj4AVAGORtwd4AVgC3gEmgBBwCPgMWANOAQ8AbwBHgHuAp4D3gLuARwoGmNUizF/j4yDC5BWM1kNvvlxFA8xikRrBxHIUhutFMBlgQoshhPphGAXe/OggKqqb2cibxwuEXjUcQjccxi5eFRL1fDSbKrUhy2CMb2aLyepkegDWsBwPlrVC0/kLHmeCBQ=='))
>>> f=open('bytecode','wb')
>>> f.write(d)
>>>
```

This gives us [the bytecode](bytecode). The file is still missing the 8 byte header that all pyc files have. To fix this, compile any py file into a pyc and do
>head -c 8 example.pyc > bytecode.pyc
>cat bytecode >> bytecode.pyc

The resulting pyc will be executable. This can now be disassembled [like this](disassembly.log).
Here we can see why the code can't be decompiled with uncompyle2 or other similar tools. The ROT_TWO instruction rotates the top two stack items. By calling two successive ROT_TWO, the stack is returned to the same state as before the instruction sequence. So, these sequences have no effect on the logic of the code, but may confuse decompilers.
Looking at the instructions, it appears to be comparing the password's characters in groups of four. Filtering out only the LOAD_CONST, we get the characters that are being compared. They are compared in reversed groups of four
>llaC em yP aht notriv lauhcamni !eac Ini npreterP tohty ntybdocese!!!ctihN{noy woc uoc naipmoa eldnur yP nnohttyb doceni euoy rb ria}!napwssro :dorWp gnssadrow...elP  esa yrtaga .ni oD tonurbf etecro)=

The 73rd to 70th and 77th to 74th characters look familiar
>hitc
on{N

following this pattern, we eventually get the flag
>hitcon{Now you can compile and run Python bytecode in your brain!}