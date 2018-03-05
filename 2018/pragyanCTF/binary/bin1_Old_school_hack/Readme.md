There are plenty of writeups that describe how to use radare2 nad GDB. in this writeup I'll describe another way to solve this challenge

First, I check the binary for any interesting strings

```
illustris@BITSkrieg:~$ strings police_academy
.
.
.
2a588070H
0ae8e5f5H
1ca9df9cH
5a44356dH
@ .dat
c85ade1cH
47bcbbe2H
ac642149H
19491b18H
@ .dat
829c1a32H
6223afb3H
3c34c16bH
ba47472dH
@ .dat
a54df28dH
b8b4d80fH
706611daH
99819460H
@ .dat
453be7bcH
0f23d90cH
0e33cd5bH
510382c0H
@ .dat
3133efc6H
92a75d5bH
d56a6e7aH
f726127cH
@ .dat
flag.txtH
.
.
.
Enter password to authentic yourself : 
kaiokenx20
.
.
.
```

Six 36 char long alphanumeric strings that end in .dat, and a string with "flag.txt". There's also a string right after the password prompt that has "kaiokenx20". This might be the password if the binary just calls a strcmp with a constant argument to compare against.

I then try running it with ltrace to see what function calls it makes
```
illustris@BITSkrieg:~$ ltrace ./police_academy
__libc_start_main(0x40099b, 1, 0x7ffc0c558168, 0x400d10 <unfinished ...>
printf("Enter password to authentic your"...)                                                                                     = 39
fflush(0x7fc7d4e8c720Enter password to authentic yourself : )                                                                                                            = 0
__isoc99_scanf(0x400e41, 0x7ffc0c558040, 0, 0x7fc7d4bb50c4
```
kaiokenx20
```
)                                                                       = 1
strncmp("kaiokenx20", "kaiokenx20", 10)                                                                                           = 0
puts("Enter case number: "Enter case number: 
)                                                                                                       = 20
printf("\n\t 1) Application_1"
)                                                                                                   = 19
printf("\n\t 2) Application_2"	 1) Application_1
)                                                                                                   = 19
printf("\n\t 3) Application_3"	 2) Application_2
)                                                                                                   = 19
printf("\n\t 4) Application_4"	 3) Application_3
)                                                                                                   = 19
printf("\n\t 5) Application_5"	 4) Application_4
)                                                                                                   = 19
printf("\n\t 6) Application_6"	 5) Application_5
)                                                                                                   = 19
printf("\n\t 7) Flag"	 6) Application_6
)                                                                                                            = 10
printf("\n\n\t Enter choice :- "	 7) Flag

)                                                                                                 = 20
fflush(0x7fc7d4e8c720	 Enter choice :- )                                                                                                            = 0
__isoc99_scanf(0x400fac, 0x7ffc0c558038, 0, 0x7fc7d4bb50c4
```
5
```
)                                                                       = 1
strlen("453be7bc0f23d90c0e33cd5b510382c0"...)                                                                                     = 36
fopen("453be7bc0f23d90c0e33cd5b510382c0"..., "r")                                                                                 = 0
printf("\nNo such record exists. Please v"...
)                                                                                    = 50
fflush(0x7fc7d4e8c720No such record exists. Please verify your choice.)                                                                                                            = 0
puts("\n"

)                                                                                                                        = 2
+++ exited (status 0) +++
```
It gets password from the user, presumably writes it into a buffer on the stack, then uses strncmp to compare the first 10 characters with kaiokenx20. It then asks for an int. If I give 5, it does strlen and fopen on the 5th string fromt he string dump above. Notice that strlen returns 36.

There's clearly a switch case that overwrites a string, say "filename". This string is then used to decide what file to open and print.
What if I don't pick a valid option in the switch case?
```
illustris@BITSkrieg:~$ ltrace ./police_academy
__libc_start_main(0x40099b, 1, 0x7ffda7477528, 0x400d10 <unfinished ...>
printf("Enter password to authentic your"...)                                                                                     = 39
fflush(0x7f4442226720Enter password to authentic yourself : )                                                                                                            = 0
__isoc99_scanf(0x400e41, 0x7ffda7477400, 0, 0x7f4441f4f0c4
```
kaiokenx20
```
)                                                                       = 1
strncmp("kaiokenx20", "kaiokenx20", 10)                                                                                           = 0
puts("Enter case number: "Enter case number: 
)                                                                                                       = 20
printf("\n\t 1) Application_1"
)                                                                                                   = 19
printf("\n\t 2) Application_2"	 1) Application_1
)                                                                                                   = 19
printf("\n\t 3) Application_3"	 2) Application_2
)                                                                                                   = 19
printf("\n\t 4) Application_4"	 3) Application_3
)                                                                                                   = 19
printf("\n\t 5) Application_5"	 4) Application_4
)                                                                                                   = 19
printf("\n\t 6) Application_6"	 5) Application_5
)                                                                                                   = 19
printf("\n\t 7) Flag"	 6) Application_6
)                                                                                                            = 10
printf("\n\n\t Enter choice :- "	 7) Flag

)                                                                                                 = 20
fflush(0x7f4442226720	 Enter choice :- )                                                                                                            = 0
__isoc99_scanf(0x400fac, 0x7ffda74773f8, 0, 0x7f4441f4f0c4
```
9
```
)                                                                       = 1
strlen("\377\377\377\377\377\377")                                                                                                = 6
printf("\nNo such record exists. Please v"...
)                                                                                    = 50
fflush(0x7f4442226720No such record exists. Please verify your choice.)                                                                                                            = 0
puts("\n"

)                                                                                                                        = 2
+++ exited (status 0) +++
```
Looks like the filename is uninitialized. But compared to above, it doesn't even reach the fopen after the strlen. Maybe the filename needs to be 36 bytes long.

Next, I try to overflow the password field
```
illustris@BITSkrieg:~$  ltrace ./police_academy
__libc_start_main(0x40099b, 1, 0x7ffddeabed78, 0x400d10 <unfinished ...>
printf("Enter password to authentic your"...)                                                                                     = 39
fflush(0x7fb5cd9ee720Enter password to authentic yourself : )                                                                                                            = 0
__isoc99_scanf(0x400e41, 0x7ffddeabec50, 0, 0x7fb5cd7170c4
```
kaiokenx20aaaabbbbccccdddd
```
)                                                                       = 1
strncmp("kaiokenx20aaaabbbbccccdddd", "kaiokenx20", 10)                                                                           = 0
puts("Enter case number: "Enter case number: 
)                                                                                                       = 20
printf("\n\t 1) Application_1"
)                                                                                                   = 19
printf("\n\t 2) Application_2"	 1) Application_1
)                                                                                                   = 19
printf("\n\t 3) Application_3"	 2) Application_2
)                                                                                                   = 19
printf("\n\t 4) Application_4"	 3) Application_3
)                                                                                                   = 19
printf("\n\t 5) Application_5"	 4) Application_4
)                                                                                                   = 19
printf("\n\t 6) Application_6"	 5) Application_5
)                                                                                                   = 19
printf("\n\t 7) Flag"	 6) Application_6
)                                                                                                            = 10
printf("\n\n\t Enter choice :- "	 7) Flag

)                                                                                                 = 20
fflush(0x7fb5cd9ee720	 Enter choice :- )                                                                                                            = 0
__isoc99_scanf(0x400fac, 0x7ffddeabec48, 0, 0x7fb5cd7170c4
```
9
```
)                                                                       = 1
strlen("bbccccdddd")                                                                                                              = 10
printf("\nNo such record exists. Please v"...
)                                                                                    = 50
fflush(0x7fb5cd9ee720No such record exists. Please verify your choice.)                                                                                                            = 0
puts("\n"

)                                                                                                                        = 2
+++ exited (status 0) +++
```

Great. anything after kaiokenx20aaaabb overflows into the filename. Now I just need to put a 32 byte string here that points to flag.txt

Final payload: `kaiokenx20aaaabb././././././././././././././flag.txt` for password, `9` for case number
