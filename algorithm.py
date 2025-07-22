from sys import stdin

stdin = open('input.txt', 'r')

n = int(stdin.readline())

dots = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())

    dots.append([x, y])

dots.sort()

a = 10