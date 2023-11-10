from random import randint, choice
from math import gcd


def gen_key():
    primes = [i for i in range(100000 + 1)]
    primes[1] = 0
    i = 2

    while i <= 100000:
        if primes[i] != 0:
            j = i + i
            while j <= 100000:
                primes[j] = 0
                j = j + i
        i += 1

    primes = [i for i in primes if (i != 0)]

    p = primes[randint(20, 30)]
    q = primes[randint(20, 30)]
    n = p * q

    f = (q - 1) * (p - 1)

    primes = [i for i in primes if (gcd(f, i) == 1) and (i < f) and (i > 20)]
    e = choice(primes)

    for i in range(f):
        if (i * e) % f == 1:
            d = i
    return('открытый ключ:{' + str(e) + '|' + str(n) + '}' + '\n' + 'закрытый ключ:{' + str(d) + '|' + str(n) + '}')
