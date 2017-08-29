import sys
import math
# import project-euler
from sets import Set

def get_proper_divisors(n):
	proper_divisors = Set([1])

	sqrt = math.sqrt(n)
	if n % sqrt == 0:
		proper_divisors.add(sqrt)

	i = 2
	while i < sqrt:
		if n % i == 0:
			proper_divisors.add(i)
			proper_divisors.add(n / i)

		i += 1

	return proper_divisors


def get_abundant_numbers_less_than(maximum):
	return filter(lambda x: sum(get_proper_divisors(x)) > x, range(1, maximum))


def get_sums_of_two_abundant_numbers_less_than(n):
	abundant_nums = get_abundant_numbers_less_than(n)

	abundant_sums = Set([])

	for i in abundant_nums:

		j = 0
		while j < len(abundant_nums) and i + abundant_nums[j] < n:
			abundant_sums.add(i + abundant_nums[j])
			j += 1

	return abundant_sums


def non_abundant_sums_less_than(t):
	abundant_sums = get_sums_of_two_abundant_numbers_less_than(t)

	total = 0
	for i in range(t):
		if i not in abundant_sums:
			total += i

	return total
















