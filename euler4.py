
def is_palindrome(N):
    to_s = str(N)
    if to_s == to_s[::-1]:
        return True
    return False


def euler4(l):
    max_factor = 10 ** l - 1
    i = max_factor
    max_palindrome = 0
    while i > 0:
        i -= 1
        j = max_factor
        while j > 0:
            j -= 1
            if is_palindrome(i*j) and (i*j > max_palindrome):
                max_palindrome = i*j
    return max_palindrome


if __name__ == '__main__':
    print euler4(3)