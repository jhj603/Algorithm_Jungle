from sys import stdin

stdin = open("input.txt", "r")

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())

    coins = list(map(int, stdin.readline().split()))

    m = int(stdin.readline())

    DP = [0 for _ in range(m + 1)]

    DP[0] = 1

    for i in coins:
        for j in range(i, m + 1):
            DP[j] += DP[j - i]

    print(DP[m])
