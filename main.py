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


m_max = 10000000



# Generate all primes until isqrt(n)
def generate_primes(n):
    res = [2]

    for i in range(3, isqrt(n) + 1):
        prime = True
        for d in res:
            if d > isqrt(i):
                break

            if i % d == 0:
                prime = False

        if prime:
            res.append(i)

    return res

primes = generate_primes(m_max)







def get_totient(n):
    res = n

    for i in primes:
        if i > n:
            break

        if n % i == 0:
            res = res * (i - 1) // i

    return res



for i in range(1, 100):
    print(f"{i} - {get_totient(i)}")



