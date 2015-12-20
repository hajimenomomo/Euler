__author__ = 'mohamed'
import math


def euler3(N):
    f = prime_factorization(N)
    return f[len(f)-1]


def prime_factorization(N):
    cnt = 1
    factor = N
    factors = []
    is_prime = False
    while cnt < math.sqrt(N):
        cnt += 1
        if factor % cnt == 0:
            factors.append(cnt)
            factor = factor / cnt
            cnt = 1
    res = N
    for i in factors:
        res = res / i
    factors.extend(full_prime_factorization(res))
    return factors


def full_prime_factorization(N):
    cnt = 1
    factor = N
    factors = []
    is_prime = False
    while cnt < N:
        cnt += 1
        if factor % cnt == 0:
            factors.append(cnt)
            factor = factor / cnt
            cnt = 1
    return factors

print euler3(600851475143)
