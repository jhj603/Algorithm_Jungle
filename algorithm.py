from sys import stdin

stdin = open("input.txt", "r")

W, H = map(int, stdin.readline().split())

wArray = [0, W]
hArray = [0, H]

N = int(stdin.readline())

for _ in range(N):
    How, Where = map(int, stdin.readline().split())

    if 0 == How:
        hArray.append(Where)
    else:
        wArray.append(Where)

wArray.sort()
hArray.sort()

maxW = max([y - x for x, y in zip(wArray, wArray[1:])])
maxH = max([y - x for x, y in zip(hArray, hArray[1:])])

print(maxH * maxW)
