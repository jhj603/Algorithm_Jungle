from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

a = 0
b = 1

for _ in range(2, n + 1):
    a, b = b, a + b

print(b)
