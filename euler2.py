__author__ = 'mohamed'
import math


def euler2(N):
    """
    even numbers of fibonacci are located every 3 terms
    :param N:
    :return:
    """
    i = 0
    current_term = 0
    res = 0
    while current_term <= N:
        res += current_term
        i += 1
        current_term = fib(3*i)
    return res


def fib(N):
    """
    This function computes fibonacci numbers using the compute by rounding method
    :param N:
    :return:
    """
    sqrt5 = math.sqrt(5)
    phi = (sqrt5 + 1) / 2
    return int(round(math.pow(phi, N) / sqrt5))


print euler2(4000000)
