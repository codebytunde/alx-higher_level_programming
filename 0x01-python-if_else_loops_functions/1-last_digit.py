#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if n >= 0:
	 nLast = n % 10:
else:
	nLast = ((n * -1) % 10) * -1
message = "Last digit of %d is %d and is" % (n, nLast)
if nLast == 0:
	 print(message, "0")
elif nLast > 5:
	print(message, "greater than 5")
elif nLast < 6 && nLast != 0:
	print(message, "less than 6 and not 0")
