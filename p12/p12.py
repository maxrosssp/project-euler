import helpers

def getLowestTriNumWithDivisorsOver(n):
	divisors = 0

	triNum = 0
	i = 1
	while divisors < n:
		triNum += i
		i += 1
		factors = helpers.getFactorsOf(triNum)

		divisors = len(factors)

	return triNum