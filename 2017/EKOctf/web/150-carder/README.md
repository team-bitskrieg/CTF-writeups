#ECOPARTY CTF 2016 : Carder
Solved by heisenberg,illustris
##Challenge

###Carder
(web, 150 points, solved by 119)
```
The fastest carder from the far west.

http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000
```

##Solution
The webpage gives the first and last four digits of a Visa card, a MasterCard and an AmEx card. We have 15 seconds to fill in the remaining digits of the card.
All credit cards follow a simple modulo 10 method for verifying the numbers. We read about it [here](http://www.freeformatter.com/credit-card-number-generator-validator.html)
Heisenberg wrote a script that reads the numbers from the webpage and generates one possible solution that satisfies the Luhn Formula.

[heisen_c4rd.py](heisen_c4rd.py)

The flag is:
>EKO{8c211399505f4f7f8cfd8f4208fe6b2e}
