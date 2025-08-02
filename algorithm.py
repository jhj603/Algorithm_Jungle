from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

matrices = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

DP = [[float("inf") for _ in range(n)] for _ in range(n)]

for i in range(n):
    DP[i][i] = 0

for i in range(1, n):
    for j in range(n - i):
        k = i + j

        for l in range(j, k):
            DP[j][k] = min(
                DP[j][k],
                DP[j][l]
                + DP[l + 1][k]
                + (matrices[j][0] * matrices[l][1] * matrices[k][1]),
            )


print(DP[0][n - 1])
