import time

def divisors(n):

    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())

    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1

                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    for factor in generate(0):
        yield factor


def proper_divisors(n):
    return list(divisors(n))[:-1]


def proper_divisors_sum(n):
    return sum(proper_divisors(n))


def is_amicable_number(n):
    m = proper_divisors_sum(n)

    divisor_sum_m = proper_divisors_sum(m)
    divisor_sum_n = m

    return m + n if m > n and divisor_sum_m == n else 0


def old_sum_of_amicable_nums_less_than(t):
    amicable_numbers = []

    amicable_sum = 0
    for n in range(t):
        if n not in amicable_numbers:
            sum_of_divisors_n = proper_divisors_sum(n)
            m = sum_of_divisors_n

            if m > n:
                sum_of_divisors_m = proper_divisors_sum(m)

                if sum_of_divisors_n == m and sum_of_divisors_m == n:
                    amicable_numbers.append(n)
                    amicable_numbers.append(m)

                    amicable_sum += n + m

    return (amicable_sum, amicable_numbers)


def sum_of_amicable_nums_less_than(t):
    amicable_sum = 0

    for n in range(t):
        amicable_sum += is_amicable_number(n)

    return (amicable_sum, [])


def solve_problem(f, f_name):
    start = time.time()
    (ans, nums) = f(10000)
    end = time.time()

    print 'Got answer: %d in %f using %s' % (ans, (end - start), f_name)

solve_problem(old_sum_of_amicable_nums_less_than, 'old_sum_of_amicable_nums_less_than')
solve_problem(sum_of_amicable_nums_less_than, 'sum_of_amicable_nums_less_than')










