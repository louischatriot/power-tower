import time
class Timer():
    def __init__(self):
        self.reset()

    def reset(self):
        self.start = time.time()

    def time(self, message = ''):
        duration = time.time() - self.start
        print(f"{message} ===> Duration: {duration}")
        self.reset()

t = Timer()





from math import isqrt, floor
import numpy


m_max = 10000000



# Generate all primes less than or equal to n
def generate_primes(n):
    res = [2, 3, 5, 7, 11]

    for i in range(13, n + 1, 2):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue

        prime = True
        for d in res:
            if d > isqrt(i):
                break

            if i % d == 0:
                prime = False

        if prime:
            res.append(i)

    return res


# Much faster than my naive method using Erathostene Sieve
# Inspired from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes_until_n(n):
    n += 1
    sieve = numpy.ones(n//2, dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return [2] + list(2*numpy.nonzero(sieve)[0][1::]+1)


def gen_primes(n):
    n = n + 1
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, isqrt(n) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = primes_until_n(m_max)


def get_totient(n):
    res = n

    for i in primes:
        if i > n // 2:
            break

        if n % i == 0:
            res = res * (i - 1) // i

    return res


# Iterative version slightly faster
def fast_exp(b, n, m):
    if n == 0:
        return 1

    b %= m

    exps = []
    while n > 0:
        if n % 2 == 0:
            exps.append(0)
            n //= 2
        else:
            exps.append(1)
            n -= 1

    res = 1
    for i in reversed(exps):
        if i == 1:
            res = (res * b) %m
        else:
            res = (res ** 2) % m

    return res

    # if n == 1:
        # return b

    # if n % 2 == 0:
        # return ((fast_exp(b, n // 2) % m) ** 2) % m
    # else:
        # return ((b % m) * (fast_exp(b, n - 1) % m)) % m







m = 53667
b = 445
N = 10000




