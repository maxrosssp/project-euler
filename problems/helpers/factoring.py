import numpy as np

def get_factors_of(n):
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
