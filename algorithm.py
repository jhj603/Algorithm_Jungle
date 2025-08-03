from sys import stdin

stdin = open("input.txt", "r")

count = 0

n, k = map(int, stdin.readline().split())

a = [int(stdin.readline()) for _ in range(n)]

for i in range(n - 1, -1, -1):
    if a[i] > k:
        continue

    count += k // a[i]
    k %= a[i]

print(count)
