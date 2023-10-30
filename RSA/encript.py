from random import randint,choice
from math import gcd

p = randint(50, 100)
q = randint(50, 100)
n = p * q

f = (q - 1) * (p - 1)
primes = [i for i in range(f + 1)]

primes[1] = 0

i = 2

while i <= f:
    if primes[i] != 0:
        j = i + i
        while j <= f:
            primes[j] = 0
            j = j + i
    i += 1

primes = [i for i in primes if (i != 0) and (gcd(f, i) == 1) and (i < f)]
e = choice(primes)

for i in range(f):
    if (i*e) % f == 1:
        d = i
print('открытый ключ:{'+ str(e) +'|'+ str(n)+'}')
print('закрытый ключ:{'+ str(d) +'|'+ str(n)+'}')

massage = 'Serega Pirat'
mass_massage = map(ord, massage)
secret_mass = []
decript_mass = []
mass_massage = list(mass_massage)

for i in mass_massage:
    secret_mass.append((i ** e) % n)
for i in secret_mass:
    decript_mass.append((i ** int(d)) % n)
secret = map(chr, decript_mass)
print(mass_massage)
print(secret_mass)
print(decript_mass)
print(''.join(secret))

decript_mass = []
