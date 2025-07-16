from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())


def fib_tail(n, first, second):
    if n == 0:
        return first

    return fib_tail(n - 1, second, first + second)


print(fib_tail(n, 0, 1))
