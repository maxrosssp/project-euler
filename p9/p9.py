def specPythagTrip():
	a = 2

	while a < 1000:
		b = 2
		c = 1000 - a - b
		while c > 0 and b < a:
			# if b == 1
			if (a**2 + b**2) == c**2:
				return a * b * c
			b += 1
			c = 1000 - a - b
		a += 1
	return 0

print(specPythagTrip())