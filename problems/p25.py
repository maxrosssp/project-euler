fibonacci_number = {
	1: 1,
	2: 1
}

def nth_fibonacci_number(n):
	if fibonacci_number.has_key(n):
		return fibonacci_number[n]
	else:
		fibonacci_number[n] = nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)
		del fibonacci_number[n - 2]
		return fibonacci_number[n]

def first_fibonacci_number_with_digits(d):
	i = 1

	lowest_allowed = 10**(d - 1)

	while nth_fibonacci_number(i) < lowest_allowed:
		i += 1

	return i

print(first_fibonacci_number_with_digits(1000))