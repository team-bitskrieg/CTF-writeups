#ECOPARTY CTF 2016 : Old but gold
Solved by heisenberg,illustris
##Challenge

###Old but gold
(misc, 250 points, solved by 76)
```
These QR codes look weird

Hint
Flag on UPPERCASE!

Attachment
```
[misc250_100ff979353dd452.zip](misc250_100ff979353dd452.zip)

##Solution

The zip file has 14 sheets of FORTRAN punch codes. [this site](https://userpages.umbc.edu/~jmartens/misc/card/index.html) shows how to decode the punch cards.
Heisenberg wrote a script that reads the images and gives the corresponding characters.

[r3ad4tran.py](r3ad4tran.py)

```
ONCE UPON A TEME, THERE WAS A YOUNG HACKER CALLED MJ                               f7191b128c49ecfef0b27cd049550ae75249f86b.png
AND COBOL, B(T EVEN AFTER ALL THOSE YEARS HE DOESNT KNOW                           a034586b253b057c96da0b6707364853886b22b6.png
MANUALS TRY1NG TO LEARN HOW TO PROGRAM AND SPEND A LOT                             4a95fea0f5e9af0af550b94fb960222e934ad09b.png
HOW TO PROPERLY MRITE SECURE CODE IN THOSE LANGUAGES                               cdeea42d7f7216f93a9f1eb93b2723c70e693bea.png
OF TIME PUNCHING THOSE NARDS, CAN YOU IMAGINE WHAT COULD                           07d561df3da01f31590066f014652e995f7b76f1.png
CARDS? AFTER THOSE HOURS WAITING ROR A RESULT, THEN IT SAYS                        a8a103961eccf8a991edfed1aaa39a8f9a3fe622.png
THE BUG, BUT THOSE WER3 THE OLD DAYS. CAN YOU FIND THE FLAG                        19756efa72339faa9c9b5fe1743c3abedbc5079d.png
USE THOSE PONCHED CARDS, HE LIKES TO PROGRAM IN FORTRAN                            89596be1f6463cb83abaecac7a375546069ecf0f.png
IN THOSE DAYS YOUR ONLY OPTION W4S READ LARGE BOOKS AND                            a9aba85ebcb160a7b18ea22abfb9589bd3ce1914.png
USING THIS OLD TECHNOLOGY? GOOD LUCK, YOU WILL NEED IT)                            24c1e220c056210e6507c4c57079ffb99ffeb96c.png
IT WAS THE SIXTIES, HE WAS TRYKNG TO FIGURE OUT HOW TO                             2d77fbd5eda9ed661a7834d8273815722fb97ccc.png
THAT WILL TAKE MORE TIME TO MEBUG AND FIGURE OUT WHERE WAS                         d3860afefe98f2408e24218a882aaf227d9287b9.png
ERROR DUE TO A SMALL AND ALMOST INSIGNIFICANT MIST4KE BUT                          93ec404ba9266f5d059a727a6460b2693fc4c440.png
HAPPEN IF YOU FAKE A SMALL MISTAKE IN ON OF THOSE PUNCHED                          85a749d44bcba42869f21fb58f9725a443066a4f.png
```

On sorting the strings, and picking out the wrong characters, we get the flag:
>M41NFR4M3