from sys import stdin

stdin = open("input.txt", "r")


def Factorial(num):
    if 1 >= num:
        return 1

    return num * Factorial(num - 1)


print(Factorial(int(stdin.readline())))
