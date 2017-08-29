import math

def nth_perm_rec(n, chars, s):
	if chars == []:
		return s

	chars_left = len(chars)

	if chars_left == 1:
		 return s + chars[0]

	f = math.factorial(chars_left - 1)
	i = n / f

	return nth_perm_rec(n % f, chars[:i] + chars[(i+1):], s + chars[i])

def nth_lexi_permutation(n, elements):
	elements.sort()

	return nth_perm_rec(n - 1, elements, '')


print(nth_lexi_permutation(1000000, [str(x) for x in range(10)]))