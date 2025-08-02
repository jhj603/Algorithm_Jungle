from sys import stdin

stdin = open("input.txt", "r")

n = int(stdin.readline())

board = [list(map(int, stdin.readline().split())) for _ in range(n)]
DP = [[float("inf") for _ in range(2**n)] for _ in range(n)]

DP[0][1] = 0

for mask in range(1, 1 << n):
    for cur in range(n):
        if not mask & (1 << cur):
            continue

        for pre in range(n):
            if not mask & (1 << pre) or pre == cur:
                continue

            pre_mask = mask ^ (1 << cur)

            if board[pre][cur]:
                DP[cur][mask] = min(DP[cur][mask], DP[pre][pre_mask] + board[pre][cur])

result = float("inf")

for i in range(1, n):
    if board[i][0] and float("inf") != DP[i][(1 << n) - 1]:
        result = min(result, DP[i][(1 << n) - 1] + board[i][0])

print(result)
