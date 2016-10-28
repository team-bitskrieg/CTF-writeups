from PIL import Image
import os
r1 = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', ":", "#", "@", "'", '=', '"']
r2 = ['&', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '[', '.', '<', '(', '+', '!']
r3 = ['-', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', ']', '$', '*', ')', ';', '^']
r4 = ['0', '/', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '\\', ',', '%', '_', '>', '?']
for pic in os.listdir('.'):
	if not pic.endswith('.py'):
		im = Image.open(pic)
		pix = im.load()
		x, y = im.size
		code = []
		for i in xrange(15, x, 7):
			_code = []
			for j in xrange(20, y, 20):
				if pix[i, j] == (255, 255, 255, 255):
					_code.append(j/20)
			code.append(_code)
		o = ''
		for x in code:
			if x:
				if x[0] == 1:
					ind = 0
					if len(x) == 2:
						ind = x[1] - 3
					if len(x) == 3:
						ind = x[1] + 5
					o += r2[ind]
				elif x[0] == 2:
					ind = 0
					if len(x) == 2:
						ind = x[1] - 3
					if len(x) == 3:
						ind = x[1] + 5
					o += r3[ind]
				elif x[0] == 3:
					ind = 0
					if len(x) == 2:
						ind = x[1] - 3
					if len(x) == 3:
						ind = x[1] + 5
					o += r4[ind]
				else:
					ind = 0
					if len(x) == 1:
						ind = x[0] - 3
					if len(x) == 2:
						ind = x[0] + 5
					o += r1[ind]					
			else:
				o += ' '
		print o, pic
