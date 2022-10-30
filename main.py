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

    for i in primes:
        if i > n:
            break

        if n % i == 0:
            res = res * (i - 1) // i

    return int(res)


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



def tower_naive(b, h, m):
    res = b
    for i in range(0, h - 1):
        res = b ** res

    res = res % m
    return res


def tower (b, h, m):
    if m == 1:
        return 0

    if b == 1 or h == 0:
        return 1

    if h == 1:
        return b % m

    totient = get_totient(m)
    sm = m * totient // gcd(m, totient)

    pos = [b % sm]

    h -= 1
    initial = 0
    while h > 0:
        a = fast_exp(b, pos[-1] % sm, sm)
        pos.append(a)
        initial += 1
        h -= 1
        if a >= m:
            break

    if h == 0:
        return pos[-1] % m

    print(pos)


    a = fast_exp(b, pos[-1] % sm, sm)
    pos.append(a)
    initial += 1
    h -= 1




    start = pos[-1]
    cycle_length = 0
    while True:
        a = fast_exp(b, pos[-1] % sm, sm)
        cycle_length += 1
        if a == start:
            break
        pos.append(a)

    # print("%%%%%%%%%%%%%%%%%%")
    # print(cycle_length)
    # print(pos)


    h -= initial
    h %= cycle_length
    h += initial

    # print(pos[h] % m)

    return pos[h] % m


    # See how fast we cycle through the same exponents
    # for i in range(0, 10):
        # a = fast_exp(b, pos[-1] % sm, sm)
        # # if a == start:
            # # break
        # pos.append(a)

    # cycle_length = len(pos) + 1


    # print("===========================")
    # print(len(pos))
    # print(pos)

    # pos = [i % m for i in pos]

    # print(pos)


    # res = pos[h % cycle_length] % m

    # return res


def tower(b, h, m):
    return tower_rec(b, h, m)


def tower_rec(b, h, m):
    # print(m)
    if m == 1:
        return 0

    if b == 1 or h == 0:
        return 1

    if h == 1:
        return b % m

    return pow(b, tower_rec(b, h - 1, get_totient(m)), m)





# b = 445
# h = 10000
# m = 53667

# for m in range(1, 20):
    # print(get_totient(m))

# 1/0


m = 1001
t_3_3 = 3 ** 3 ** 3
t_3_4 = pow(3, t_3_3, m)
# test.assert_equals(tower(3, 4, m), t_3_4)




t_2_4 = pow(2, 2 ** 2 ** 2)
t_2_5 = pow(2, t_2_4, 720)
t_2_6 = pow(2, 720 + t_2_5, m)
# test.assert_equals(tower(2, 6, m), t_2_6)




t.reset()

# res = tower_naive(2, 6, 1001)
# print(res)

# res = tower(3, 3, 1546)
res = tower(4, 3, 10)   # Should equal 6
# res = tower(3, 3, 25)
# res = tower_rec(3, 3, 25)

print(res)


t.time("Towered")





