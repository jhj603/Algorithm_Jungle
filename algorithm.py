from sys import stdin

stdin = open("input.txt", "r")


def Factorial(num):
    if 1 >= num:
        return 1

    return num * Factorial(num - 1)


def Factorial_tail(num, sum):
    if 0 == num:
        return sum

    return Factorial_tail(num - 1, sum * num)


n = int(stdin.readline())

print(Factorial(n))
print(Factorial_tail(n, 1))
