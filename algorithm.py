from sys import stdin

stdin = open("input.txt", "r")


def nsum(n):
    if n == 0:
        return 0

    return n + nsum(n - 1)


def nexponentiation(b, n):
    if 0 == n:
        return 1

    if not n % 2:
        return nexponentiation(b, n // 2) ** 2
    else:
        return b * nexponentiation(b, n - 1)


def tail_nexpo(b, n, cur):
    if 0 == n:
        return cur

    return tail_nexpo(b, n - 1, cur * b)


def fib(n):
    if 0 == n:
        return 0

    if 1 == n:
        return 1

    return fib(n - 1) + fib(n - 2)


print(nsum(5))
print(nexponentiation(2, 2))
print(tail_nexpo(2, 2, 1))
