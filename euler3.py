__author__ = 'mohamed'
import math

,,,,,,,,,,
def euler3(N):
    f = prime_factorization(N)
    return f[len(f)-1]


def prime_factorization(N):
    cnt = 2
    factor = N
    factors = []
    while cnt < N:
        if factor % cnt == 0:
            factors.append(cnt)
            factor = N // cnt
        else:
            cnt += 1
    return factors


def primes_up_to(N):
    primality = [True] * (N+1)
    primality[0] = False
    for i in range(2, N+1):
        if primality[i]:
            for j in range(2, (N // i) + 1):
                primality[i*j] = False
    result = []
    for number, prime in enumerate(primality):
        if prime:
            result.append(number)
    return result

print euler3(600851475143)
