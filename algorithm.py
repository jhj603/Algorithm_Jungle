from sys import stdin

stdin = open("input.txt", "r")

first = stdin.readline().strip()
second = stdin.readline().strip()

first_len = len(first)
second_len = len(second)

DP = [[0 for _ in range(second_len + 1)] for _ in range(first_len + 1)]

for i in range(1, first_len + 1):
    for j in range(1, second_len + 1):
        if first[i - 1] == second[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[first_len][second_len])
