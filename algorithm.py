from sys import stdin

stdin = open('input.txt', 'r')

Prime = [True] * 10001

Prime[0] = Prime[1] = False

for i in range(2, int(10001 ** 0.5) + 1):
    if Prime[i]:
        for j in range(i * i, 10001, i):
            Prime[j] = False

T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())

    for i in range(N // 2, 1, -1):
        if Prime[i] and Prime[N - i]:
            print(f"{i} {N - i}")
            break