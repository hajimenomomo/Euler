__author__ = 'mohamed'


def euler1(N):
    m = (N - 1) // 3
    sum3n = 3 * (m * (m + 1) / 2)
    m = (N - 1) // 5
    sum5n = 5 * (m * (m + 1) / 2)
    m = (N - 1) // 15
    sum15n = 15 * (m * (m + 1) / 2)
    return sum3n + sum5n - sum15n

print euler1(1000)