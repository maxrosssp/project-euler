from helpers.primes import *

primes = get_primes_less_than(10000)

def make_quad_func(a, b):

	def quad_func(n):
		return (n**2) + (a * n) + b

	return quad_func

def get_num_consec_primes_produced(a, b):
	maximum = max(a, b)
	f = make_quad_func(a, b)

	num_primes = 0
	for i in range(maximum):
		if f(i) in primes:
			num_primes += 1
		else:
			return num_primes


	return num_primes

def get_max_consec_primes(max_a, max_b):
	maximum = 0
	prod = 0

	for a in range(max_a * -1, max_a):
		for b in range(max_b * -1, max_b):
			num = get_num_consec_primes_produced(a, b)
			if num > maximum:
				maximum = num
				prod = a * b

		print a

	return prod

def solution(max_a, max_b)
	return get_max_consec_primes(max_a, max_b)


