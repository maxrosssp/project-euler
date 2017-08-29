def isPallindrome(n):
	nStr = str(n)
	nStrLen = len(nStr)
	mid = nStrLen / 2

	i = 0
	while i < mid:
		if nStr[i] != nStr[(nStrLen - 1) - i]:
			return False
		i += 1

	return True

print('True: '),
print(isPallindrome(123321))

print('True: '),
print(isPallindrome(1235321))

print('False: '),
print(isPallindrome(123421))

print('False: '),
print(isPallindrome(124321))

def findLargestPallindrome():
	x = 999
	largestPallindrome = 0

	while x > 0:
		if largestPallindrome > (x * 999):
			return largestPallindrome

		y = x
		while y <= 999:
			prod = x * y
			if isPallindrome(prod) and prod > largestPallindrome:
				largestPallindrome = prod
			y += 1

		x -= 1

	return largestPallindrome


print(findLargestPallindrome())