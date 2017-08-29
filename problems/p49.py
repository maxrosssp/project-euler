import helpers as h

primes = [x for x in h.getPrimesLessThan(10000) if x >= 1000]

def findPrimePerms(primes):
	for p in primes:
		permutations = [q for q in primes if sorted(str(p)) == sorted(str(q))]

		for i in range(len(permutations)):
			testPerm = permutations[i]
			for perm in [n for n in permutations if n > testPerm]:
				if perm + (perm - testPerm) in permutations:
					return testPerm, perm, perm + (perm - testPerm)

			i += 1
			primes.remove(testPerm)

print(findPrimePerms(primes))