from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

DP = [[float("inf") for _ in range(n)] for _ in range(n)]

matrices = [list(map(int, stdin.readline().split())) for _ in range(n)]

for i in range(n):
    DP[i][i] = 0

for i in range(2, n + 1):
    for j in range(n - i + 1):
        for k in range(j, i + j - 1):
            matrix_mul = matrices[j][0] * matrices[k][1] * matrices[i + j - 1][1]

            cur_total = DP[j][k] + DP[k + 1][i + j - 1] + matrix_mul

            DP[j][i + j - 1] = min(DP[j][i + j - 1], cur_total)

print(DP[0][n - 1])
