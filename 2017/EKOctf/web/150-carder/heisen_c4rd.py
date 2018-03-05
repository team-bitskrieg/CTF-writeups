hue = """


Eyy h4x0r! Gimme valid numbers!


Visa
4485
rest of your number
1200
Mastercard
5274
rest of your number
3838
American Express
3432
rest of your number
9938
"""

def sol(a, b, t):
	a, b = map(int, list(str(a))), map(int, list(str(b)))
	l = b[-1]
	c = a + [0 for i in xrange(5 + t)] + b[:-1]
	c = c[::-1]
	d = c[:]
	tot = 0
	for i in xrange(len(c)):
		if i % 2 == 0:
			d[i] += d[i]
		if d[i] > 9:
			d[i] -= 9
	diff = ((10 - l) - (sum(d) % 10)) % 10
	for i in xrange(5, len(c) - 3, 2):
		while diff and c[i] < 9:
			c[i] += 1
			diff -= 1
	c = c[::-1] + [l]
	return ''.join(map(str, c))[4:-4]

a, b, c, d, e, f = hue.split("\n")[6::2]
print sol(a, b, 0)
print sol(c, d, 3)
print sol(e, f, 2)
