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


# Iterative version slightly faster
# But Python's pow better than both
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





from math import isqrt, floor, gcd
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

    if n == 1 or n == 2:
        return 1

    if n == 3:
        return 2

    if n % 2 == 0:
        return 2 * get_totient(n // 2)

    for i in primes:
        if i > n:
            break

        if n % i == 0:
            res = res * (i - 1) // i

    return int(res)


def tower_naive(b, h, m):
    res = b
    for i in range(0, h - 1):
        res = b ** res

    res = res % m
    return res


def tower(b, h, m):
    return tower_rec(b, h, m)


def tower_rec(b, h, m):
    if m == 1:
        return 0

    if b == 1 or h == 0:
        return 1

    if h == 1:
        return b % m

    # if m == 2:
        # return b % 2

    # if h == 2:
        # return pow(b, 2, m)

    totient = get_totient(m)
    previous = tower_rec(b, h - 1, totient)

    temp = 1
    large = False
    for i in range(1, h):
        temp = b ** temp
        if temp >= totient:
            large = True
            break

    if gcd(b, m) == 1 or not large:
        return pow(b, previous, m)
    else:
        return ( pow(b, previous, m) * pow(b, totient, m) ) % m







m = 1001
t_3_3 = 3 ** 3 ** 3
t_3_4 = pow(3, t_3_3, m)

t_2_4 = pow(2, 2 ** 2 ** 2)
t_2_5 = pow(2, t_2_4, 720)
t_2_6 = pow(2, 720 + t_2_5, m)


# Format is (b, h, m, result)
tests = [
    (4, 3, 10, 6),
    (2, 4, 1000, 536),
    (2, 2, 1000, 4),
    (2, 3, 100000, 16),
    (7, 1, 5, 2),
    (3, 4, 1001, t_3_4),
    (2, 6, 1001, t_2_6),
    (35274318940391579706, 72714099242717105322, 7808487, 7475019)
    ]


t.reset()


for b, h, m, result in tests:
    res = tower(b, h, m)
    print(f"{res} should be equal to {result}")



t.time("Towered")





