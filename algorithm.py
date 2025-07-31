from sys import stdin

stdin = open("input.txt", "r")

first = stdin.readline().strip()
second = stdin.readline().strip()

first_size = len(first)
second_size = len(second)

DP = [[0 for _ in range(first_size + 1)] for _ in range(second_size + 1)]

for i in range(1, second_size + 1):
    for j in range(1, first_size + 1):
        if first[j - 1] == second[i - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

print(DP[second_size][first_size])
