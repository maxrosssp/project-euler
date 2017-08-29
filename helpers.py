import time
import numpy as np

def getPrimesLessThan(n):
    correction = (n%6>1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5 : n + 1}[n % 6]
    sieve = [True] * (n / 3)
    sieve[0] = False
    for i in xrange((int(n**0.5) / 3) + 1):
      if sieve[i]:
        k = (3 * i) + 1 | 1
        sieve[((k * k) / 3)::(2 * k)] = [False] * (((n / 6) - ((k * k) / 6) - 1) / k + 1)
        sieve[(((k * k) + (4 * k) - (2 * k * (i & 1))) / 3)::(2 * k)] = [False] * ((((n / 6) - (((k * k) + (4 * k) - (2 * k * (i & 1))) / 6) - 1) / k) + 1)
    return [2, 3] + [(3 * i) + 1 | 1 for i in xrange(1, (n / 3) - correction) if sieve[i]]


def getFactorsOf(n):
    low_factors = []
    high_factors = []

    root = int(np.ceil(n**0.5))

    for i in range(1, root):
        if n % i == 0:
            low_factors.append(i)
            high_factors.insert(0, n / i)

    if root * root == n:
        low_factors.append(root)

    return low_factors + high_factors


def getTimedFunction(func):
    def timedFunction(*args):
        start = time.time()
        result = func(*args)
        end = time.time()

        return (result, end - start)

    return timedFunction