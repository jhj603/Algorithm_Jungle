from sys import stdin

stdin = open("input.txt", "r")

# 1차원 배열을 이용한 최적화된 풀이
n, k = map(int, stdin.readline().split())

DP = [0 for _ in range(k + 1)]

for _ in range(n):
    w, v = map(int, stdin.readline().split())

    for i in range(k, w - 1, -1):
        DP[i] = max(DP[i], v + DP[i - w])

print(DP[k])

# 2차원 배열을 이용한 정석 풀이
# n, k = map(int, stdin.readline().split())

# DP = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# for i in range(1, n + 1):
#     w, v = map(int, stdin.readline().split())

#     for j in range(1, k + 1):
#         if j < w:
#             DP[i][j] = DP[i - 1][j]
#         else:
#             DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - w] + v)

# print(DP[n][k])
