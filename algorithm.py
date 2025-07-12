from sys import stdin

stdin = open("input.txt", "r")

N = int(stdin.readline())

HowMany = 0

col = [False for _ in range(N)]
ld = [False for _ in range(N * 2 - 1)]
rd = [False for _ in range(N * 2 - 1)]


def DFS(Count):
    global HowMany

    if N == Count:
        HowMany += 1
        return

    for i in range(N):
        if (0 == col[i]) and (0 == rd[(N - 1) + (Count - i)]) and (0 == ld[Count + i]):
            col[i] = rd[((N - 1) + (Count - i))] = ld[Count + i] = True
            DFS(Count + 1)
            col[i] = rd[((N - 1) + (Count - i))] = ld[Count + i] = False


DFS(0)

print(HowMany)
