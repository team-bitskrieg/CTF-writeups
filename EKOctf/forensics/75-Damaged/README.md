#ECOPARTY CTF 2016 : Damaged
Solved by illustris,HSR0,lum0s
##Challenge

###Damaged
```
All you have to do is to see this damaged image!

Attachment
[for75_165560e4a08b23f7.zip](for75_165560e4a08b23f7.zip)
```

##Solution

First we read about the [BMP file structure on Wikipedia](https://en.wikipedia.org/wiki/BMP_file_format)
Then we compared the hex dump of a normal BMP with that of the corrupted one to see what was different.

Normal:
![bump](example.bmp)
Damaged:
![bump](damaged.png)

In the normal image, 15th byte onwards is
>28 00 00 00

which is the start of the DIB header. The corrupted image appears to be starting from the DIB header. We just need to append the BMP header to the start of the file.
To do this, first we filles the missing 14 bytes as
>42 4d AA AA AA AA 00 00 00 00 BB BB BB BB

We then replaced BB BB BB BB with the offset of the pixel array. THis is easy to identify, as it looks like a block of FFs in this case. The starting address is 36, written as 36 00 00 00 in little endian form. Lastly, we calculated the new size of the file and replaced AA AA AA AA with 36 75 00 00.

The image can now be opened.
![bump](out.bmp)