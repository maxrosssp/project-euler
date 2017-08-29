import time

def smallestMultiple(ns):
	ns.sort()

	if ns[0] == 0:
		return 0

	res = 1
	for i in range(len(ns)):
		res *= ns[i]
		ns = [n / ns[i] if n % ns[i] == 0 else n for n in ns]

	return res


start = time.time()
print(smallestMultiple(range(1, 20)))
end = time.time()
print(end - start)