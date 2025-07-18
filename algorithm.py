from sys import stdin

stdin = open("input.txt", "r")

a, b, c = map(int, stdin.readline().split())


def multi(count):
    if 1 == count:
        return a % c

    temp = multi(count // 2)

    if count % 2:
        return (temp * temp * (a % c)) % c
    else:
        return (temp * temp) % c


print(multi(b))
