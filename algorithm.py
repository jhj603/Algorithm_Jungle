from sys import stdin

stdin = open("input.txt", "r")

n, k = map(int, stdin.readline().split())

DP = [0 for _ in range(k + 1)]

for _ in range(n):
    w, v = map(int, stdin.readline().split())

    for i in range(k, w - 1, -1):
        DP[i] = max(DP[i], DP[i - w] + v)

print(DP[k])
